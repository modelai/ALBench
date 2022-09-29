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

_EXCLUDED_SET_PREFIX=$4
_MINED_SET_PREFIX=$5
MIR_ROOT=$6
TMP_MINING_ROOT=$7
MINING_TOPK=$8
YMIR_MODEL_LOCATION=$9
YMIR_ASSET_LOCATION=${10}
MEDIA_CACHE_PATH=${11}
CUR_DIR=${12}
MDOEL_NAME=${13}
DATASET_NAME=${14}
EXECUTOR=${15}
AL_ALGO=${16}
mining() {
    if [[ $# -lt 3 ]]; then
        echo "exclude needs cycle num and model hash, abort" >&2
        exit 1
    fi

    if [[ $2 -ge 0 ]]; then
        _echo_in_color $C_YELLOW "mining from $_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2 to $_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2"
        $MIR_EXE mining --root $MIR_ROOT \
                        --src-revs "$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                        --dst-rev "$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                        -w "$TMP_MINING_ROOT/$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                        --topk $MINING_TOPK \
                        --model-location "$YMIR_MODEL_LOCATION" \
                        --media-location "$YMIR_ASSET_LOCATION" \
                        --model-hash $3 \
                        --cache $MEDIA_CACHE_PATH \
                        --task-config-file "$CUR_DIR/mining-config.yaml" \
                        --executor $EXECUTOR
    else
        echo "invalid cycle num: $2, abort" >&2
        exit 1
    fi
}

post_mining_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 join $2"
    echo "  or: run $0 outlabel $2"
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