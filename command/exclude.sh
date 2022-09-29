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


MINING_SET_PREFIX=$3
_MERGED_TRAINING_SET_PREFIX=$4
_EXCLUDED_SET_PREFIX=$5
MDOEL_NAME=$6
DATASET_NAME=$7
MIR_ROOT=$8
AL_ALGO=$9
exclude() {
    if [[ $# < 2 ]]; then
        echo "exclude needs cycle num, abort" >&2
        exit 1
    fi

    if [[ $2 -eq 0 ]]; then
        # first exclude merge:
        _echo_in_color $C_YELLOW \
                       "exclude from $MINING_SET_PREFIX - $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0 to $_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0"
        $MIR_EXE merge --root $MIR_ROOT \
                       --src-revs "$MINING_SET_PREFIX@$MINING_SET_PREFIX" \
                       --ex-src-revs "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0" \
                       --dst-rev "$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0@$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0" \
                       -s host
    elif [[ $2 -gt 0 ]]; then
        _PREVIOUS_CYCLE_NUM=$(($2 - 1))
        _echo_in_color $C_YELLOW \
                       "exclude from $_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_PREVIOUS_CYCLE_NUM - $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2 to $_EXCLUDED_SET_PREFIX-$2"
        $MIR_EXE merge --root $MIR_ROOT \
                       --src-revs "$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_PREVIOUS_CYCLE_NUM@$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$_PREVIOUS_CYCLE_NUM" \
                       --ex-src-revs "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       --dst-rev "$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2@$_EXCLUDED_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-$2" \
                       -s host
    else
        echo "invalid cycle num: $2, abort" >&2
        exit 1
    fi
}

post_exclude_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 mining $2 <model-hash> (model-hash: hash of the model you just trained)"
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