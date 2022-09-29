#!/bin/bash
YMIR_MODEL_LOCATION=$2
C_GREEN=$3
C_OFF='\033[0m'
C_RED='\033[0;31m'
C_GREEN="\033[0;32m"
C_YELLOW='\033[0;33m'
C_RED_BOLD='\033[1;31m'
C_GREEN_BOLD='\033[1;32m'
C_YELLOW_BOLD='\033[1;33m'
init() {
    # YMIR_MODEL_LOCATION and YMIR_ASSET_LOCATION should exists
    # init MIR_ROOT
    # RAW_DATA_ROOT should exists
    echo "$YMIR_MODEL_LOCATION"
    if ! [[ -d $YMIR_MODEL_LOCATION ]]; then
        mkdir $YMIR_MODEL_LOCATION
    fi
     _echo_in_color $C_GREEN "$1 success"
}
_echo_in_color() {
    printf $1
    printf "${*:2}\n"
    printf $C_OFF
}
show_help_info() {
    _echo_in_color $C_OFF "ymir-0.1.1" 2 3 4
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