# ALBench
## ALBench Leaderboard for active learning in object detection
**we offer a leaderborad for active learning in object detection in [here](http://120.77.255.232/)** 
## Introduction
 Active learning has been popular
in image classification, but has not been fully explored in object detection. Most of current
works on object detection are evaluated with different settings, making it difficult to fairly
compare their performance. To facilitate the research in this field, this paper contributes an
active learning benchmark framework named as ALBench for evaluating active learning
in object detection. Developed on an automatic deep model training system, this ALBench
framework is easy-to-use, compatible with different active learning algorithms, and ensures
the same training and testing protocols. We hope this automated benchmark system help
researchers to easily reproduce literature's performance and have fair comparisons with
prior arts

## Project structure
```
├── download_dataset.py
├── infer-config.yaml
├── training-config.yaml
├── mining-config.yaml
├── labels.yaml
├── README.md
├── requirements.txt
├── run.py
├── run.sh
├── init_trainSet_5000.txt
├── command
    ├── deinit.sh
    ├── exclude.sh
    ├── import.sh
    ├── init.sh
    ├── join.sh
    ├── merge.sh
    ├── mining.sh
    ├── test.sh
    └── training.sh
├── data
│   ├── COCO
│   │   ├──labels.yaml
│   │   ├── annotations
│   │   │   └── xml
│   │   ├── test2017
│   │   ├── train2017
│   │   └── val2017
│   ├── mining
│   │   ├── anno
│   │   └── img
│   ├── train
│   │   ├── anno
│   │   └── img
│   └── val
│       ├── anno
│       └── img
└── utils
    └── generate_dataset.py
    └── coco2voc.py
```
## Installation
### Prerequisites
Follow the [INSTALL.md](https://github.com/IndustryEssentials/ymir#2-installation) to install ymir first
```
pip install -r requirements.txt
```


## Dataset download
1. Download COCO dataset
```
ALBench_path$ python utils/download_dataset.py
```
2. Organize the dataset: 
```
ALBench_path$ cd utils
ALBench_path/utils$ python coco2voc.py
ALBench_path/utils$ python generate_dataset.py
```
dataset should be organized as following
```
ALBench/
├── data/
│   ├── COCO/
│   │   ├── mining/
│   │   │   ├── anno/
│   │   │   └── img/
│   │   ├── train/
│   │   │   ├── anno/
│   │   │   └── img/
│   │   ├── val/
│   │   │   ├── anno/
│   │   │   └── img/
```
## Build Ymir executor
ALBench is based on Ymir system, detector and active learning algorithm should be build as  docker image. To build your own Ymir executor, or get our official executor, see [build ymir executor](https://github.com/modelai/ymir-executor-fork/tree/ymir-dev#build-ymir-executor) for detail
## modify config file
1. modify ALBench_config.yaml based on the instuction below
```
# your user name and password for ALBench Leaderboard if you want result automatically uploaded to leaderboard
user_name: ""
password: ''

# 1 if you using any other training strategy,such as semi-supervised learning , else 0
leaderboard_id: 1  

# detector and training_docker are paired
detector : ['YOLOV5','SSD']
training_docker: ['youdaoyzbx/ymir-executor:ymir1.1.0-YOLOV5','youdaoyzbx/ymir-executor:ymir1.1.0-SSD']

# mining_algo and mining_docker are paired
mining_algo: [cald]
mining_docker: ['youdaoyzbx/ymir-executor:ymir1.1.0-cald']
```
## Usage
```
sh run.sh
```
training and mining result will be listed in 
```
ALBench_path/tmp/training
ALBench_path/tmp/mining
```