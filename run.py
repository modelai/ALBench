import argparse
import json
import logging
from opcode import opname
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pandas as pd
import requests
import yaml

VERBOSE = str(os.getenv('ALBench_VERBOSE', True)).lower() == 'true'  # global verbose mode


def set_logging(name=None, verbose=VERBOSE):
    rank = int(os.getenv('RANK', -1))  # rank in world for Multi-GPU trainings
    level = logging.INFO if verbose and rank in {-1, 0} else logging.ERROR
    log = logging.getLogger(name)
    log.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    handler.setLevel(level)
    log.addHandler(handler)


set_logging()  # run before defining LOGGER
LOGGER = logging.getLogger("ALBench")  # define globally (used in train.py, val.py, detect.py, etc.)


class ALBench():
    def __init__(self):
        super().__init__()
        self.MIR_EXE = "mir"
        self.CUR_DIR = os.getcwd()  # your working directory
        self.MIR_ROOT = self.CUR_DIR + "/mir-demo-repo"

        self.YMIR_MODEL_LOCATION = self.CUR_DIR + "/ymir-models"
        self.YMIR_ASSET_LOCATION = self.CUR_DIR + "/ymir-assets"

        self.CLASS_TYPES = "expose_rubbish"
        self.MINING_TOPK = str(500)  #! FOR TEST
        self.RAW_DATA_ROOT = ''
        self.RAW_TRAINING_SET_IMG_ROOT = ''
        self.RAW_VAL_SET_IMG_ROOT = ''
        self.RAW_MINING_SET_IMG_ROOT = ''
        self.TMP_TRAINING_ROOT = self.CUR_DIR + "/tmp/training"
        self.TMP_MINING_ROOT = self.CUR_DIR + "/tmp/mining"
        self.TMP_OUTLABEL_ASSET_ROOT = self.CUR_DIR + "/tmp/outlabel/assets"
        self.TMP_INLABEL_ANNOTATION_ROOT = self.CUR_DIR + "/tmp/inlabel/annotations"
        self.MEDIA_CACHE_PATH = self.CUR_DIR + "/cache"

        self.MODEL_HASH_TXT_DIR = self.CUR_DIR + '/model-hash-txt'
        self.RESULT_ROOT = self.CUR_DIR + '/result'
        self.model_hash_txt_path = None
        self.model_hash = []
        self.user_name = ""
        self.leaderboard_id = ""
        self.training_docker = ''
        self.mining_algo = ''
        self.detector = ''

    def check_status(self, code):
        if code != 0:
            exit()

    def get_dataset_path(self, dataset):
        self.CUR_DIR = os.getcwd()

        self.RAW_DATA_ROOT = os.path.join(self.CUR_DIR, 'data', dataset)  #! you can change
        print(self.RAW_DATA_ROOT)
        # in this pipeline, the whole data is devided into 3 part: TRAINING_SET, the VAL_SET and the MINING_SET
        # TRAINING_SET and VAL_SET are used to train the first version of model
        # and MINING_SET used to mining datas with command mir mining
        #   and the mining result will be merged into the previous training set
        self.RAW_TRAINING_SET_IMG_ROOT = self.RAW_DATA_ROOT + "/train/img"  #! you can change
        self.RAW_TRAINING_SET_ANNO_ROOT = self.RAW_DATA_ROOT + "/train/anno"  #! you can change
        self.RAW_TRAINING_SET_INDEX_PATH = self.RAW_DATA_ROOT + "/train-short.txt"  #! you can change

        self.RAW_VAL_SET_IMG_ROOT = self.RAW_DATA_ROOT + "/val/img"  #! you can change
        self.RAW_VAL_SET_ANNO_ROOT = self.RAW_DATA_ROOT + "/val/anno"  #! you can change
        self.RAW_VAL_SET_INDEX_PATH = self.RAW_DATA_ROOT + "/val.txt"  #! you can change

        self.RAW_MINING_SET_IMG_ROOT = self.RAW_DATA_ROOT + "/mining/img"  #! you can change
        self.RAW_MINING_SET_ANNO_ROOT = self.RAW_DATA_ROOT + "/mining/anno"  #! you can change
        self.RAW_MINING_SET_INDEX_PATH = self.RAW_DATA_ROOT + "/mining.txt"  #! you can change, FOR TEST

        self.TRAINING_SET_PREFIX = dataset + "-training"
        self.MINING_SET_PREFIX = dataset + "-mining"  #! you can change
        self.VAL_SET_PREFIX = dataset + "-val"  #! you can change

        self._MERGED_TRAINING_SET_PREFIX = "cycle-node-tr-and-va"
        self._TRAINED_TRAINING_SET_PREFIX = "cycle-node-trained"
        self._EXCLUDED_SET_PREFIX = "cycle-node-excluded"
        self._MINED_SET_PREFIX = "cycle-node-mined"
        self._INLABELED_SET_PREFIX = "cycle-node-inlabeled"

    def generate_txtfile(self, img_root, index_path):
        path_list = os.listdir(img_root)
        with open(index_path, 'w') as f:
            for file_name in path_list:
                abs_file_path = Path(os.path.join(img_root, file_name)).absolute()
                f.write((str(abs_file_path)) + '\n')

    def deinit(self):
        deinit_param = [
            self.YMIR_ASSET_LOCATION, self.YMIR_MODEL_LOCATION, self.MIR_ROOT, self.CUR_DIR, self.MODEL_HASH_TXT_DIR
        ]
        deinit_command = ' ./command/deinit.sh  deinit '
        # os.system(deinit_command+' '.join(init_param))
        p = subprocess.Popen(deinit_command + ' '.join(deinit_param), shell=True)
        return_code = p.wait()
        print('return_code_deinit', return_code)
        self.check_status(return_code)

    def initing(self, dataset):

        init_param = [
            self.YMIR_MODEL_LOCATION, self.YMIR_ASSET_LOCATION, self.RAW_TRAINING_SET_IMG_ROOT,
            self.RAW_TRAINING_SET_ANNO_ROOT, self.RAW_VAL_SET_IMG_ROOT, self.RAW_VAL_SET_ANNO_ROOT,
            self.RAW_MINING_SET_IMG_ROOT, self.RAW_MINING_SET_ANNO_ROOT, self.RAW_TRAINING_SET_INDEX_PATH,
            self.RAW_VAL_SET_INDEX_PATH, self.RAW_MINING_SET_INDEX_PATH, self.TRAINING_SET_PREFIX, self.VAL_SET_PREFIX,
            self.MINING_SET_PREFIX, self.MIR_ROOT, self.CUR_DIR, self.MEDIA_CACHE_PATH, self.MODEL_HASH_TXT_DIR
        ]

        init_command = ' ./command/init.sh  init '
        p = subprocess.Popen(init_command + ' '.join(init_param), shell=True)

        return_code = p.wait()

        self.check_status(return_code)
        if os.path.isdir(os.path.join(self.MIR_ROOT, '.mir')):
            shutil.copy(os.path.join(self.RAW_DATA_ROOT, 'labels.yaml'), os.path.join(self.MIR_ROOT, '.mir'))

        self.generate_txtfile(self.RAW_TRAINING_SET_IMG_ROOT, self.RAW_TRAINING_SET_INDEX_PATH)
        self.generate_txtfile(self.RAW_VAL_SET_IMG_ROOT, self.RAW_VAL_SET_INDEX_PATH)
        self.generate_txtfile(self.RAW_MINING_SET_IMG_ROOT, self.RAW_MINING_SET_INDEX_PATH)

    def importing(self):
        import_param = [
            self.TRAINING_SET_PREFIX, self.MIR_ROOT, self.RAW_TRAINING_SET_INDEX_PATH, self.RAW_TRAINING_SET_ANNO_ROOT,
            self.YMIR_ASSET_LOCATION, self.VAL_SET_PREFIX, self.RAW_VAL_SET_INDEX_PATH, self.RAW_VAL_SET_ANNO_ROOT,
            self.MINING_SET_PREFIX, self.RAW_MINING_SET_INDEX_PATH, self.RAW_MINING_SET_ANNO_ROOT
        ]

        import_command = ' ./command/import.sh  import '
        p = subprocess.Popen(import_command + ' '.join(import_param), shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    def merge(self, model, dataset, al_algo):
        merge_param = [
            self.MIR_ROOT, self.TRAINING_SET_PREFIX, self.VAL_SET_PREFIX, self._MERGED_TRAINING_SET_PREFIX, model,
            dataset, al_algo
        ]
        merge_command = ' ./command/merge.sh merge '
        p = subprocess.Popen(merge_command + ' '.join(merge_param), shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    def training(self, cycle, model, dataset, al_algo, excutor, training_config):
        training_param = [
            self._MERGED_TRAINING_SET_PREFIX, self._TRAINED_TRAINING_SET_PREFIX, self.MIR_ROOT, self.TMP_TRAINING_ROOT,
            self.YMIR_MODEL_LOCATION, self.YMIR_ASSET_LOCATION, self.CUR_DIR, excutor, model, dataset, al_algo, training_config
        ]
        training_command = ' ./command/training.sh training ' + str(cycle) + ' '

        p = subprocess.Popen(training_command + ' '.join(training_param), shell=True)

        return_code = p.wait()

        self.check_status(return_code)
        self.model_hash_txt_path = os.path.join(
            self.MODEL_HASH_TXT_DIR, self._TRAINED_TRAINING_SET_PREFIX + '-' + model + '-' + dataset + '-' + al_algo + '.txt')
        if os.listdir(self.YMIR_MODEL_LOCATION):
            for model_hash in os.listdir(self.YMIR_MODEL_LOCATION):
                if model_hash not in self.model_hash:
                    self.model_hash.append(model_hash)
                    with open(self.model_hash_txt_path, 'a') as f:
                        f.write(str(model_hash) + '\n')

    def exclude(self, cycle, model, dataset, al_algo):
        exclude_param = [
            self.MINING_SET_PREFIX, self._MERGED_TRAINING_SET_PREFIX, self._EXCLUDED_SET_PREFIX, model, dataset,
            self.MIR_ROOT, al_algo
        ]
        exclude_command = ' ./command/exclude.sh exclude ' + str(cycle) + ' '
        p = subprocess.Popen(exclude_command + ' '.join(exclude_param), shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    def mining(self, cycle, model, dataset, al_algo, executor, mining_config):
        with open(self.model_hash_txt_path, 'r') as f:
            model_hashes = f.readlines()
        model_hash = model_hashes[cycle].strip()

        mining_param = [
            self._EXCLUDED_SET_PREFIX, self._MINED_SET_PREFIX, self.MIR_ROOT, self.TMP_MINING_ROOT, self.MINING_TOPK,
            self.YMIR_MODEL_LOCATION, self.YMIR_ASSET_LOCATION, self.MEDIA_CACHE_PATH, self.CUR_DIR, model, dataset,
            executor, al_algo , mining_config
        ]
        mining_command = ' ./command/mining.sh mining ' + str(cycle) + ' ' + str(model_hash) + ' '
        p = subprocess.Popen(mining_command + ' '.join(mining_param), shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    def join(self, cycle, model, dataset, al_algo):
        join_param = [self._MERGED_TRAINING_SET_PREFIX, self._MINED_SET_PREFIX, self.MIR_ROOT, model, dataset, al_algo]
        join_command = './command/join.sh join ' + str(cycle) + ' '
        p = subprocess.Popen(join_command + ' '.join(join_param), shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    def get_map(self, i, model, dataset, al_algo):
        trained_dir_name = self._MERGED_TRAINING_SET_PREFIX + '-' + model + '-' + dataset + '-' + al_algo + '-' + str(i)
        print(os.path.join(self.TMP_TRAINING_ROOT, trained_dir_name, 'out/models/result.yaml'))
        file = open(os.path.join(self.TMP_TRAINING_ROOT, trained_dir_name, 'out/models/result.yaml'))
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        # class_ap = data['class_aps']
        map = data['map']
        return float(map)

    def save_statistic(self):
        if not os.path.isdir(self.RESULT_ROOT):
            os.mkdir(self.RESULT_ROOT)
        shutil.copy(self.TMP_MINING_ROOT)

    def upload_result(self, file):
        dfile = open(file)
        url_official = "http://113.100.143.90:5000/file"
        test_res_official = requests.post(url_official, files={"file": dfile})
        if test_res_official.ok:
            print('ok')
        else:
            print('not')

    def upload_config(self, data):
        data = json.dumps(data)
        url_official = "http://113.100.143.90:5000/config"
        test_res_official = requests.post(url_official, data)
        response = json.loads(test_res_official.text)
        if response['code'] == 404:
            print(response['message'])
            print(response['url'])
            exit(0)

    def check_config(self, config):
        data = yaml.load(open(config), Loader=yaml.FullLoader)
        auto_upload = True
        user_name = data['user_name']
        token = data['token']

        if not user_name or not token:
            auto_upload = False

        try:
            leaderboard_id = data['leaderboard_id']
            training_docker = data['training_docker']
            mining_algo = data['mining_algo']
            detector = data['detector']
            if not training_docker or not mining_algo:
                raise ValueError(config + ': please specify training docker and mining algo')
            if len(detector)!=len(training_docker):
                raise ValueError(config + ': please specify detector name based on training docker')
            if leaderboard_id not in [0, 1]:
                raise ValueError(config + ': leaderboard_id should  be 0 or 1')

        except ValueError as e:
            print(repr(e))
            exit(0)
        if auto_upload:
            self.upload_config(data)
        self.user_name = user_name
        self.leaderboard_id = str(leaderboard_id)
        self.training_docker = training_docker
        self.mining_algo = list(map(lambda x:x.upper(),mining_algo))
        self.detector = list(map(lambda x:x.upper(),detector))
        return auto_upload

    def update_mining_config(self, mining_config_file, mining_algo):
        mining_data = yaml.load(open(mining_config_file), Loader=yaml.FullLoader)
        mining_data['executor_config']['mining_algorithm'] = mining_algo
        with open(mining_config_file, 'w') as f:
            yaml.dump(mining_data, f)

    def check_dataset(self):
        flage = True
        if not os.path.isdir(self.RAW_DATA_ROOT):
            from utils import download_dataset,coco2voc,generate_dataset
            download_dataset.download_data()
            coco2voc.COCO2VOC()
            generate_dataset.generate_dataset()
        if not os.path.isfile(os.path.join(self.RAW_DATA_ROOT,'labels.yaml')):
            shutil.copy('labels.yaml',self.RAW_DATA_ROOT)
        if not os.path.isdir(self.RAW_TRAINING_SET_IMG_ROOT):
            flage = False
            LOGGER.info('train dir not exist')
        if not os.path.isdir(self.RAW_VAL_SET_IMG_ROOT):
            flage = False
            LOGGER.info('val dir not exist')
        if not os.path.isdir(self.RAW_MINING_SET_IMG_ROOT):
            flage = False
            LOGGER.info('mining dir not exist')
        if not flage:
            exit(0)

    def main(self, opt):

        auto_apload = self.check_config(opt.ALBench_config)
        exit()
        csv_file_name = self.user_name + '_' + opt.dataset + '_' + self.leaderboard_id + '_' + 'result_public.csv'
        txt_name = self.user_name + '_' + opt.dataset + '_' + self.leaderboard_id + '_' + 'result_public.txt'
        df1 = pd.DataFrame(columns=['Dataset', 'Detector', 'AL_algo', 'Baseline', 'iter1', 'iter2', 'iter3', 'iter4'])
        df_content = []
        dataset_all = opt.dataset.split(',')

        # self.deinit()
        for dataset in dataset_all:
            self.get_dataset_path(dataset)
            self.check_dataset()
            # self.initing(dataset)

            # self.importing()
            print(opt.mining_config,opt.training_config)
            for model_index in range(len(self.detector)):
                for al_algo_index in range(len(self.mining_algo)):
                    self.update_mining_config(opt.mining_config, self.mining_algo[al_algo_index])
                    self.merge(self.detector[model_index], dataset, self.mining_algo[al_algo_index])
                    df_content = [dataset, self.detector[model_index], self.mining_algo[al_algo_index]]
                    with open(txt_name,'a') as f:
                        f.write('\n')
                        f.write(','.join(df_content))

                    for i in range(opt.iters + 1):
                        self.training(i, self.detector[model_index], dataset, self.mining_algo[al_algo_index],
                                      self.training_docker[model_index],opt.training_config)
                        self.exclude(i, self.detector[model_index], dataset, self.mining_algo[al_algo_index])

                        self.mining(i, self.detector[model_index], dataset, self.mining_algo[al_algo_index],
                                    self.training_docker[model_index],opt.mining_config)
                        self.join(i, self.detector[model_index], dataset, self.mining_algo[al_algo_index])
                        
                        map = self.get_map(i, self.detector[model_index], dataset, self.mining_algo[al_algo_index])
                        df_content.append(map)

                        with open(txt_name,'a') as f:
                            f.write(','+str(map))

                    df4 = pd.DataFrame(df_content).T

                    df4.columns = df1.columns

                    df1 = pd.concat([df1, df4], ignore_index=True)
            df1.to_csv(csv_file_name, index=None)
            if auto_apload:
                self.upload_result(csv_file_name)

    def parse_opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--dataset', type=str, default='COCO')
        parser.add_argument('--iters', type=int, default=4) # Do 4 mining , don't change it
        parser.add_argument('--ALBench-config', type=str, default='ALBench_config.yaml')
        parser.add_argument('--training-config', type=str, default='training-config.yaml')
        parser.add_argument('--mining-config', type=str, default='mining-config.yaml')

        return parser.parse_args()


if __name__ == '__main__':
    albench = ALBench()
    opt = albench.parse_opt()
    albench.main(opt)
