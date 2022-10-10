import os,shutil,random

sample = random.sample(os.listdir('./data/COCO/train2017/'),5000)
for name in sample:
    with open('./train_5000.txt','a') as f:
        f.write(name+'\n')
