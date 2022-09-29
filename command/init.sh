#!/bin/bash
set -e # stop when any step fails.
# global variables
MIR_EXE="mir"
# CUR_DIR="$PWD"  # your working directory
# MIR_ROOT="$CUR_DIR/mir-demo-repo"

# YMIR_MODEL_LOCATION="$CUR_DIR/ymir-models"
# YMIR_ASSET_LOCATION="$CUR_DIR/ymir-assets"
# RAW_DATA_ROOT="$CUR_DIR/data/COCO"  #! you can change

# # in this pipeline, the whole data is devided into 3 part: TRAINING_SET, the VAL_SET and the MINING_SET
# # TRAINING_SET and VAL_SET are used to train the first version of model
# # and MINING_SET used to mining datas with command mir mining
# #   and the mining result will be merged into the previous training set
# RAW_TRAINING_SET_IMG_ROOT="$RAW_DATA_ROOT/train/img"  #! you can change
# RAW_TRAINING_SET_ANNO_ROOT="$RAW_DATA_ROOT/train/anno"  #! you can change
# RAW_TRAINING_SET_INDEX_PATH="$RAW_DATA_ROOT/train-short.txt"  #! you can change

# RAW_VAL_SET_IMG_ROOT="$RAW_DATA_ROOT/val/img"  #! you can change
# RAW_VAL_SET_ANNO_ROOT="$RAW_DATA_ROOT/val/anno"  #! you can change
# RAW_VAL_SET_INDEX_PATH="$RAW_DATA_ROOT/val.txt"  #! you can change

# RAW_MINING_SET_IMG_ROOT="$RAW_DATA_ROOT/train/img"  #! you can change
# RAW_MINING_SET_ANNO_ROOT="$RAW_DATA_ROOT/train/anno"  #! you can change
# RAW_MINING_SET_INDEX_PATH="$RAW_DATA_ROOT/mining.txt"  #! you can change, FOR TEST

# CLASS_TYPES="expose_rubbish"
# MINING_TOPK=50  #! FOR TEST

# TRAINING_SET_PREFIX="dataset-training"  #! you can change
# VAL_SET_PREFIX="dataset-val"  #! you can change
# MINING_SET_PREFIX="dataset-mining"  #! you can change

# TMP_TRAINING_ROOT="$CUR_DIR/tmp/training"
# TMP_MINING_ROOT="$CUR_DIR/tmp/mining"
# TMP_OUTLABEL_ASSET_ROOT="$CUR_DIR/tmp/outlabel/assets"
# TMP_INLABEL_ANNOTATION_ROOT="$CUR_DIR/tmp/inlabel/annotations"
# MEDIA_CACHE_PATH="$CUR_DIR/cache"

# _MERGED_TRAINING_SET_PREFIX="cycle-node-tr-and-va"
# _TRAINED_TRAINING_SET_PREFIX="cycle-node-trained"
# _EXCLUDED_SET_PREFIX="cycle-node-excluded"
# _MINED_SET_PREFIX="cycle-node-mined"
# _INLABELED_SET_PREFIX="cycle-node-inlabeled"

# colors
C_OFF='\033[0m'
C_RED='\033[0;31m'
C_GREEN='\033[0;32m'
C_YELLOW='\033[0;33m'
C_RED_BOLD='\033[1;31m'
C_GREEN_BOLD='\033[1;32m'
C_YELLOW_BOLD='\033[1;33m'
YMIR_MODEL_LOCATION=$2
YMIR_ASSET_LOCATION=$3
RAW_TRAINING_SET_IMG_ROOT=$4
RAW_TRAINING_SET_ANNO_ROOT=$5
RAW_VAL_SET_IMG_ROOT=$6
RAW_VAL_SET_ANNO_ROOT=$7
RAW_MINING_SET_IMG_ROOT=$8
RAW_MINING_SET_ANNO_ROOT=$9
RAW_TRAINING_SET_INDEX_PATH=${10}
RAW_VAL_SET_INDEX_PATH=${11}
RAW_MINING_SET_INDEX_PATH=${12}
TRAINING_SET_PREFIX=${13}
VAL_SET_PREFIX=${14}
MINING_SET_PREFIX=${15}
MIR_ROOT=${16}
CUR_DIR=${17}
MEDIA_CACHE_PATH=${18}
MODEL_HASH_TXT_DIR=${19}

# sub commands
init() {
    # YMIR_MODEL_LOCATION and YMIR_ASSET_LOCATION should exists
    # init MIR_ROOT
    # RAW_DATA_ROOT should exists
    if ! [[ -d $YMIR_MODEL_LOCATION ]]; then
        mkdir $YMIR_MODEL_LOCATION
    fi
    if ! [[ -d $YMIR_ASSET_LOCATION ]]; then
        mkdir -p $YMIR_ASSET_LOCATION
    fi
    if ! [[ -d $MODEL_HASH_TXT_DIR ]]; then
        mkdir $MODEL_HASH_TXT_DIR
    fi
    #check raw dataset's assets and annotation dirs, make sure that they are exist
    _RAW_DATASET_ROOTS_=($RAW_TRAINING_SET_IMG_ROOT $RAW_TRAINING_SET_ANNO_ROOT \
                         $RAW_VAL_SET_IMG_ROOT $RAW_VAL_SET_ANNO_ROOT \
                         $RAW_MINING_SET_IMG_ROOT $RAW_MINING_SET_ANNO_ROOT)
    for _DATASET_ROOT_ in "${_RAW_DATASET_ROOTS_[@]}"; do
        if ! [[ -d $_DATASET_ROOT_ ]]; then
            echo "$_DATASET_ROOT_ is not a dir, abort" >&2
            exit 1
        fi
    done
    # check raw dataset's index files
    _RAW_DATASET_INDEX_PATHS_=($RAW_TRAINING_SET_INDEX_PATH $RAW_VAL_SET_INDEX_PATH $RAW_MINING_SET_INDEX_PATH)
    for _INDEX_PATH_ in "${_RAW_DATASET_INDEX_PATHS_[@]}"; do
        if ! [[ -f $_INDEX_PATH_ ]]; then
            echo "$_INDEX_PATH_ is not a file, abort" >&2
            exit 1
        fi
    done
    # check dataset prefix, they are used in task ids, branch names and dataset names
    if [[ -z $TRAINING_SET_PREFIX || -z $VAL_SET_PREFIX || -z $MINING_SET_PREFIX ]]; then
        echo "invalid train / val / mining dataset prefix, abort" >&2
        exit 1
    fi

    # check MIR_ROOT
    if [[ -d $MIR_ROOT ]]; then
        echo "$MIR_ROOT already exists, you can:"
        echo "    rm it and init again if you just want a new mir repo"
        echo "    or run deinit to REMOVE ALL THINGS and start over again"
    else
        mkdir -p $MIR_ROOT; cd $MIR_ROOT; mir init
    fi

    # check tmp
    if ! [[ -d $CUR_DIR/tmp ]]; then
        mkdir -p $CUR_DIR/tmp
    fi

    # check cache
    if ! [[ -d $MEDIA_CACHE_PATH ]]; then
        mkdir -p $MEDIA_CACHE_PATH
    fi
}

post_init_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 import"
}

deinit() {
    if [[ -d $YMIR_ASSET_LOCATION ]]; then
        rm -rf $YMIR_ASSET_LOCATION
    fi
    if [[ -d $YMIR_MODEL_LOCATION ]]; then
        rm -rf $YMIR_MODEL_LOCATION
    fi
    if [[ -d $MIR_ROOT ]]; then
        rm -rf $MIR_ROOT
    fi
    if [[ -d $CUR_DIR/tmp ]]; then
        rm -rf $CUR_DIR/tmp
    fi
}


show_help_info() {
    _echo_in_color $C_OFF "ymir-0.1.1" 2 3 4
}

# private: colors
_echo_in_color() {
    printf $1
    printf "${*:2}\n"
    printf $C_OFF
}

# main
main() {
    # source demo-fzp.sh <command> <args>
    # call sub command in $1 directly
    if [[ $# -eq 0 ]]; then
        show_help_info
    else
        $1 "$@"
        post_$1_success "$@"
    fi
}

main "$@"