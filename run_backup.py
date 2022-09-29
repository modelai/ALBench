from cgitb import text
import code
import json
import shutil
from signal import raise_signal
import sys,os,inspect
import time
import requests

from pathlib import Path
import subprocess
import yaml
import argparse
import pandas as pd
class ALBench():

    def __init__(self):
        super().__init__()
        self.MIR_EXE="mir"
        self.CUR_DIR=   os.getcwd()# your working directory
        self.MIR_ROOT=self.CUR_DIR+"/mir-demo-repo"

        self.YMIR_MODEL_LOCATION=self.CUR_DIR+"/ymir-models"
        self.YMIR_ASSET_LOCATION=self.CUR_DIR+"/ymir-assets"
 
        self.CLASS_TYPES="expose_rubbish"
        self.MINING_TOPK=str(500)  #! FOR TEST


        self.TMP_TRAINING_ROOT=self.CUR_DIR+"/tmp/training"
        self.TMP_MINING_ROOT=self.CUR_DIR+"/tmp/mining"
        self.TMP_OUTLABEL_ASSET_ROOT=self.CUR_DIR+"/tmp/outlabel/assets"
        self.TMP_INLABEL_ANNOTATION_ROOT=self.CUR_DIR+"/tmp/inlabel/annotations"
        self.MEDIA_CACHE_PATH=self.CUR_DIR+"/cache"

        self.MODEL_HASH_TXT_DIR=self.CUR_DIR+'/model-hash-txt'
        self.RESULT_ROOT=self.CUR_DIR+'/result'
        self.model_hash_txt_path=None
        self.model_hash=[]
        self.user_name=""
        self.leaderboard_id=""
        # self.TRAINING_SET_PREFIX=None

    def check_status(self,code):
        if code!=0:
            exit()

    def get_dataset_path(self,dataset):
        self.CUR_DIR=   os.getcwd()
        
        self.RAW_DATA_ROOT=  os.path.join(self.CUR_DIR,'data',dataset)#! you can change
        print( self.RAW_DATA_ROOT)
        # in this pipeline, the whole data is devided into 3 part: TRAINING_SET, the VAL_SET and the MINING_SET
        # TRAINING_SET and VAL_SET are used to train the first version of model
        # and MINING_SET used to mining datas with command mir mining
        #   and the mining result will be merged into the previous training set
        self.RAW_TRAINING_SET_IMG_ROOT=self.RAW_DATA_ROOT+"/train/img"  #! you can change
        self.RAW_TRAINING_SET_ANNO_ROOT=self.RAW_DATA_ROOT+"/train/anno"  #! you can change
        self.RAW_TRAINING_SET_INDEX_PATH=self.RAW_DATA_ROOT+"/train-short.txt"  #! you can change

        self.RAW_VAL_SET_IMG_ROOT=self.RAW_DATA_ROOT+"/val/img"  #! you can change
        self.RAW_VAL_SET_ANNO_ROOT=self.RAW_DATA_ROOT+"/val/anno"  #! you can change
        self.RAW_VAL_SET_INDEX_PATH=self.RAW_DATA_ROOT+"/val.txt"  #! you can change

        self.RAW_MINING_SET_IMG_ROOT=self.RAW_DATA_ROOT+"/mining/img"  #! you can change
        self.RAW_MINING_SET_ANNO_ROOT=self.RAW_DATA_ROOT+"/mining/anno"  #! you can change
        self.RAW_MINING_SET_INDEX_PATH=self.RAW_DATA_ROOT+"/mining.txt"  #! you can change, FOR TEST

        self.TRAINING_SET_PREFIX=dataset+"-training"
        self.MINING_SET_PREFIX=dataset+"-mining"  #! you can change
        self.VAL_SET_PREFIX=dataset+"-val"  #! you can change

        self._MERGED_TRAINING_SET_PREFIX="cycle-node-tr-and-va"
        self._TRAINED_TRAINING_SET_PREFIX="cycle-node-trained"
        self._EXCLUDED_SET_PREFIX="cycle-node-excluded"
        self._MINED_SET_PREFIX="cycle-node-mined"
        self._INLABELED_SET_PREFIX="cycle-node-inlabeled"

    def generate_txtfile(self,img_root,index_path):
        path_list=os.listdir(img_root)
        with open(index_path,'w') as f:
            for file_name in path_list:
                abs_file_path =Path(os.path.join(img_root,file_name)).absolute()
                f.write((str(abs_file_path))+'\n')

    def deinit(self):
        deinit_param=[self.YMIR_ASSET_LOCATION,self.YMIR_MODEL_LOCATION,self.MIR_ROOT,self.CUR_DIR,self.MODEL_HASH_TXT_DIR]
        deinit_command = ' ./command/deinit.sh  deinit '
        # os.system(deinit_command+' '.join(init_param))
        p = subprocess.Popen(deinit_command+' '.join(deinit_param),shell=True)
        return_code = p.wait()
        print('return_code_deinit',return_code)
        self.check_status(return_code)

    def initing(self,dataset):
        self.get_dataset_path(dataset)

        init_param=[self.YMIR_MODEL_LOCATION,self.YMIR_ASSET_LOCATION,self.RAW_TRAINING_SET_IMG_ROOT,self.RAW_TRAINING_SET_ANNO_ROOT,\
            self.RAW_VAL_SET_IMG_ROOT, self.RAW_VAL_SET_ANNO_ROOT, self.RAW_MINING_SET_IMG_ROOT, self.RAW_MINING_SET_ANNO_ROOT,\
                self.RAW_TRAINING_SET_INDEX_PATH, self.RAW_VAL_SET_INDEX_PATH, self.RAW_MINING_SET_INDEX_PATH, self.TRAINING_SET_PREFIX,\
                    self.VAL_SET_PREFIX, self.MINING_SET_PREFIX, self.MIR_ROOT, self.CUR_DIR, self.MEDIA_CACHE_PATH,self.MODEL_HASH_TXT_DIR]

        init_command = ' ./command/init.sh  init '
        p = subprocess.Popen(init_command+' '.join(init_param),shell=True)

        return_code = p.wait()

        self.check_status(return_code)
        if os.path.isdir(os.path.join(self.MIR_ROOT,'.mir')):
            shutil.copy(os.path.join(self.RAW_DATA_ROOT,'labels.yaml'),os.path.join(self.MIR_ROOT,'.mir'))

        self.generate_txtfile( self.RAW_TRAINING_SET_IMG_ROOT,self.RAW_TRAINING_SET_INDEX_PATH)
        self.generate_txtfile( self.RAW_VAL_SET_IMG_ROOT,self.RAW_VAL_SET_INDEX_PATH)
        self.generate_txtfile(  self.RAW_MINING_SET_IMG_ROOT,self.RAW_MINING_SET_INDEX_PATH)

        
    
    def importing(self):
        import_param=[self.TRAINING_SET_PREFIX,self.MIR_ROOT, self.RAW_TRAINING_SET_INDEX_PATH,self.RAW_TRAINING_SET_ANNO_ROOT,\
        self.YMIR_ASSET_LOCATION, self.VAL_SET_PREFIX, self.RAW_VAL_SET_INDEX_PATH, self.RAW_VAL_SET_ANNO_ROOT, self.MINING_SET_PREFIX,\
        self.RAW_MINING_SET_INDEX_PATH, self.RAW_MINING_SET_ANNO_ROOT]
    
        import_command = ' ./command/import.sh  import '
        p = subprocess.Popen(import_command+' '.join(import_param),shell=True)
        return_code = p.wait()

        self.check_status(return_code)


    def merge(self,model,dataset,al_algo):
        merge_param=[self.MIR_ROOT,self.TRAINING_SET_PREFIX,self.VAL_SET_PREFIX,self._MERGED_TRAINING_SET_PREFIX,\
            model,dataset,al_algo]
        merge_command = ' ./command/merge.sh merge '
        p = subprocess.Popen(merge_command+' '.join(merge_param),shell=True)
        return_code = p.wait()

        self.check_status(return_code)


    def training(self,cycle,model,dataset,al_algo,excutor):
        training_param=[self._MERGED_TRAINING_SET_PREFIX,self._TRAINED_TRAINING_SET_PREFIX,self.MIR_ROOT,self.TMP_TRAINING_ROOT,\
            self.YMIR_MODEL_LOCATION,self.YMIR_ASSET_LOCATION,self.CUR_DIR,excutor,model,dataset,al_algo]
        training_command = ' ./command/training.sh training '+str(cycle)+' '

        p = subprocess.Popen(training_command+' '.join(training_param),shell=True)

        return_code = p.wait()

        self.check_status(return_code)
        self.model_hash_txt_path =os.path.join(self.MODEL_HASH_TXT_DIR,self._TRAINED_TRAINING_SET_PREFIX+'-'+model+'-'+dataset+'.txt')
        if os.listdir(self.YMIR_MODEL_LOCATION):
            for model_hash in  os.listdir(self.YMIR_MODEL_LOCATION):
                if model_hash not in self.model_hash:
                    self.model_hash.append(model_hash)
                    with open( self.model_hash_txt_path,'a') as f:
                        f.write(str(model_hash)+'\n')


    def exclude(self,cycle,model,dataset,al_algo):
        exclude_param=[self.MINING_SET_PREFIX, self._MERGED_TRAINING_SET_PREFIX, self._EXCLUDED_SET_PREFIX, model,dataset,self.MIR_ROOT,al_algo]
        exclude_command= ' ./command/exclude.sh exclude '+str(cycle)+' '
        p = subprocess.Popen(exclude_command+' '.join(exclude_param),shell=True)
        return_code = p.wait()

        self.check_status(return_code)


    def mining(self,cycle,model,dataset,al_algo,executor):
        with open(self.model_hash_txt_path,'r') as f:   
            model_hashes = f.readlines()
        model_hash = model_hashes[cycle].strip()

        mining_param=[self._EXCLUDED_SET_PREFIX, self._MINED_SET_PREFIX,self.MIR_ROOT,self.TMP_MINING_ROOT, self.MINING_TOPK,\
            self.YMIR_MODEL_LOCATION,self.YMIR_ASSET_LOCATION,self.MEDIA_CACHE_PATH,self.CUR_DIR,model,dataset,executor,al_algo]
        mining_command= ' ./command/mining.sh mining '+str(cycle)+' '+str(model_hash)+' '
        p = subprocess.Popen(mining_command+' '.join(mining_param),shell=True)
        return_code = p.wait()

        self.check_status(return_code)

    
    def join(self,cycle,model,dataset,al_algo):
        join_param=[self._MERGED_TRAINING_SET_PREFIX,self._MINED_SET_PREFIX,self.MIR_ROOT,model,dataset,al_algo]
        join_command='./command/join.sh join '+str(cycle)+' '
        p = subprocess.Popen(join_command+' '.join(join_param),shell=True)
        return_code = p.wait()


        self.check_status(return_code)


    def get_map(self,i,model,dataset,al_algo):
        trained_dir_name =self._MERGED_TRAINING_SET_PREFIX+'-'+model+'-'+dataset+'-'+al_algo+'-'+str(i)
        print(os.path.join(self.TMP_TRAINING_ROOT,trained_dir_name,'out/models/result.yaml'))
        file = open(os.path.join(self.TMP_TRAINING_ROOT,trained_dir_name,'out/models/result.yaml'))
        file_data = file.read()
        file.close()
        data = yaml.load(file_data,Loader=yaml.FullLoader)
        # class_ap = data['class_aps']
        map = data['map']
        return float(map)
    
    def save_statistic(self):
        if not os.path.isdir(self.RESULT_ROOT):
            os.mkdir(self.RESULT_ROOT)
        shutil.copy(self.TMP_MINING_ROOT)

    def upload_result(self,file):
        dfile =open(file)
        url_official="http://120.77.255.232/file"
        test_res_official = requests.post(url_official,files={"file":dfile})
        if test_res_official.ok:
            print('ok')
        else:
            print('not')

    def upload_config(self,data):
        data = json.dumps(data)
        # url="http://192.168.11.166:5000/public"
        # test_res = requests.post(url,files={"file":dfile})
        url_official="http://120.77.255.232/config"
        test_res_official = requests.post(url_official,data)
        response = json.loads(test_res_official.text)
        if response['code']==404:
            print(response['message'])
            print(response['url'])
            exit(0)


    def check_config(self,config):
        data = yaml.load(open(config),Loader=yaml.FullLoader)

        try:
            user_name = data['user_name']
            password = data['password']
            leaderboard_id=data['leaderboard_id']

            if not user_name or not password :
                raise ValueError(config+' should not be empty')
            if leaderboard_id not in [0,1]:
                raise ValueError(config+' leaderboard_id should  be 0 or 1')
        except ValueError as e:
            print(repr(e))
            exit(0)
        self.upload_config(data)
        self.user_name=user_name
        self.leaderboard_id=str(leaderboard_id)



    def main(self,opt):
        self.check_config(opt.config)
        csv_file_name=self.user_name+'_'+self.leaderboard_id+'_'+'result_public.csv'
       
        df1 = pd.DataFrame(columns = ['Dataset','Detector','AL_algo','Baseline','iter1','iter2','iter3','iter4'])
        df_content = []
        dataset_all=opt.dataset.split(',')
        models_all=opt.detector.split(',')
        AL_algo_all=opt.AL_model.split(',')
        self.deinit()
        for dataset in dataset_all:
            self.initing(dataset)
            self.importing()
            for model in models_all:
                for al_algo in AL_algo_all:
                    self.merge(model,dataset,al_algo)
                    df_content = [dataset,model,al_algo]
                    for i in range(opt.epochs+1):
                        self.training(i,model,dataset,al_algo,'youdaoyzbx/ymir-executor:ymir1.1.0-sample-tmi')
                        self.exclude(i,model,dataset,al_algo)
                        self.mining(i,model,dataset,al_algo,'youdaoyzbx/ymir-executor:ymir1.1.0-sample-tmi')
                        self.join(i,model,dataset,al_algo)
                        df_content.append( self.get_map(i,model,dataset,al_algo))
                    df4 = pd.DataFrame(df_content).T

                    df4.columns = df1.columns

                    df1 = pd.concat([df1,df4],ignore_index=True)
            df1.to_csv(csv_file_name, index=None)
            self.upload_result(csv_file_name)
    def  parse_opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--dataset',type=str, default='COCO')
        parser.add_argument('--detector',type=str,default='YOLOV5')
        parser.add_argument('--AL_model',type=str,default='CALD')
        parser.add_argument('--epochs',type=int,default=1)
        parser.add_argument('--config',type=str,default='ALBench_config.yaml')
        return parser.parse_args()



if __name__ =='__main__':
    albench = ALBench()
    opt = albench.parse_opt()
    albench.main(opt)