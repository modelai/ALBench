import shutil
import os
from tqdm import tqdm
import logging

logging.getLogger().setLevel(logging.INFO)

def generate_dataset():
    init_trainName = 'init_trainSet_5000.txt'
    train_dir = os.path.join(os.path.pardir,'data','train')
    val_dir = os.path.join(os.path.pardir,'data','val')
    mining_dir = os.path.join(os.path.pardir,'data','mining')

    def makeDir(path):
        if not os.path.isdir(path):
            os.makedirs(os.path.join(path,'img'))
            os.makedirs(os.path.join(path,'anno'))


    makeDir(train_dir)
    makeDir(val_dir)       
    makeDir(mining_dir)       

    all_train = os.listdir(os.path.join(os.path.pardir,'data','COCO','train2017'))
    logging.info('generating val set')
    for img_name in tqdm(os.listdir(os.path.join(os.path.pardir,'data','COCO','val2017'))):
        
        shutil.copy(os.path.join(os.path.pardir,'data','COCO','val2017',img_name),os.path.join(val_dir,'img',img_name))
        anno_name = img_name.split('.')[0]+'.xml'
        shutil.copy(os.path.join(os.path.pardir,'data','COCO','annotations','xml',anno_name),os.path.join(val_dir,'anno',anno_name))

    with open (os.path.join(os.path.pardir,init_trainName),'r') as f:
        logging.info('generating train set')

        for name in tqdm(f.readlines()):
            name = name.strip()

            all_train.remove(name)
            shutil.copy(os.path.join(os.path.pardir,'data','COCO','train2017',name),os.path.join(train_dir,'img',name))
            anno_name = name.split('.')[0]+'.xml'
            shutil.copy(os.path.join(os.path.pardir,'data','COCO','annotations','xml',anno_name),os.path.join(train_dir,'anno',anno_name))
        
        logging.info('generating mining set')

        for name in tqdm(all_train):
            shutil.copy(os.path.join(os.path.pardir,'data','COCO','train2017',name),os.path.join(mining_dir,'img',name))
            anno_name = name.split('.')[0]+'.xml'

            shutil.copy(os.path.join(os.path.pardir,'data','COCO','annotations','xml',anno_name),os.path.join(mining_dir,'anno',anno_name))

generate_dataset()