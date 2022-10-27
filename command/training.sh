#!/bin/bash
set -e # stop when any step fails.
MIR_EXE="mir"
# colors
C_OFF='\033[0m'
C_RED='\033[0;31m'
C_GREEN='\033[0;32m'
C_YELLOW='\033[0;33m'
C_RED_BOLD='\033[1;31m'
C_GREEN_BOLD='\033[1;32m'
C_YELLOW_BOLD='\033[1;33m'
_MERGED_TRAINING_SET_PREFIX=$3
_TRAINED_TRAINING_SET_PREFIX=$4
MIR_ROOT=$5
TMP_TRAINING_ROOT=$6
YMIR_MODEL_LOCATION=$7
YMIR_ASSET_LOCATION=$8
CUR_DIR=$9
EXECUTOR=${10}
MDOEL_NAME=${11}
DATASET_NAME=${12}
AL_ALGO=${13}
TRAINING_CONFIG=${14}



training() {
    # prepare and training
    if [[ $# -lt 2 ]]; then
        echo "training needs cycle num, abort" >&2
        exit 1
    fi
    if [[ $2 -ge 0 ]]; then
        # exit 1
        # training
        _echo_in_color $C_YELLOW "training from $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2 to $_TRAINED_TRAINING_SET_PREFIX-$2"
        $MIR_EXE train --root $MIR_ROOT \
                       -w "$TMP_TRAINING_ROOT/$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       --model-location "$YMIR_MODEL_LOCATION" \
                       --media-location "$YMIR_ASSET_LOCATION" \
                       --src-revs "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       --dst-rev "$_TRAINED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_TRAINED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       --task-config-file "$CUR_DIR/$TRAINING_CONFIG" \
                       --executor $EXECUTOR
    else
        echo "invalid cycle num: $2, abort" >&2
        exit 1
    fi
}

post_training_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 exclude $2"
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