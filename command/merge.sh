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

MIR_ROOT=$2
TRAINING_SET_PREFIX=$3
VAL_SET_PREFIX=$4
_MERGED_TRAINING_SET_PREFIX=$5
MDOEL_NAME=$6
DATASET_NAME=$7
AL_ALGO=$8
# first merge: _MERGED_TRAINING_SET_PREFIX-0 = tr:TRAINING_SET_PREFIX + va: VAL_SET_PREFIX
merge() {
    _echo_in_color $C_YELLOW "merge from tr:$TRAINING_SET_PREFIX + va:$VAL_SET_PREFIX to $_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0"
    $MIR_EXE merge --root $MIR_ROOT \
                    --src-revs "tr:$TRAINING_SET_PREFIX@$TRAINING_SET_PREFIX;va:$VAL_SET_PREFIX@$VAL_SET_PREFIX" \
                    --dst-rev "$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0@$_MERGED_TRAINING_SET_PREFIX-$MDOEL_NAME-$DATASET_NAME-$AL_ALGO-0" \
                    -s host
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