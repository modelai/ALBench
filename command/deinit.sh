#!/bin/bash
set -e # stop when any step fails.
# global variables
MIR_EXE="mir"
YMIR_ASSET_LOCATION=$2
YMIR_MODEL_LOCATION=$3
MIR_ROOT=$4
CUR_DIR=$5
MODEL_HASH_TXT_DIR=$6
# colors
C_OFF='\033[0m'
C_RED='\033[0;31m'
C_GREEN='\033[0;32m'
C_YELLOW='\033[0;33m'
C_RED_BOLD='\033[1;31m'
C_GREEN_BOLD='\033[1;32m'
C_YELLOW_BOLD='\033[1;33m'
deinit() {
    if [[ -d $YMIR_ASSET_LOCATION ]]; then
        rm -rf $YMIR_ASSET_LOCATION
    fi
    if [[ -d $YMIR_MODEL_LOCATION ]]; then
        rm -rf $YMIR_MODEL_LOCATION
    fi
    if [[ -d $MODEL_HASH_TXT_DIR ]]; then
        rm -rf $MODEL_HASH_TXT_DIR
    fi
    if [[ -d $MIR_ROOT ]]; then
        rm -rf $MIR_ROOT
    fi
    if [[ -d $CUR_DIR/tmp ]]; then
        rm -rf $CUR_DIR/tmp
    fi
}

post_deinit_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 init"
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