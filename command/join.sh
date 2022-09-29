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
_MINED_SET_PREFIX=$4
MIR_ROOT=$5
MDOEL_NAME=$6
DATASET_NAME=$7
AL_ALGO=$8
join() {
    if [[ $# -lt 2 ]]; then
        echo "join needs cycle num, abort" >&2
        exit 1
    fi

    if [[ $2 -ge 0 ]]; then
        _NEXT_CYCLE_NUM=`expr $2 + 1`
        _echo_in_color $C_YELLOW \
                       "merge topk from $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2 + tr:$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2 to $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_NEXT_CYCLE_NUM"
        $MIR_EXE merge --root $MIR_ROOT \
                       --src-revs "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2;tr:$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_MINED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       --dst-rev "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_NEXT_CYCLE_NUM@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_NEXT_CYCLE_NUM" \
                       -s host
    else
        echo "invalid cycle num: $2, abort" >&2
        exit 1
    fi
}

post_join_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 training `expr $2 + 1`"
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
        # post_$1_success "$@"
    fi
}

main "$@"