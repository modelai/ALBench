#!/bin/bash
set -e # stop when any step fails.
MIR_EXE="mir"
TRAINING_SET_PREFIX=$2
MIR_ROOT=$3
RAW_TRAINING_SET_INDEX_PATH=$4
RAW_TRAINING_SET_ANNO_ROOT=$5
YMIR_ASSET_LOCATION=$6
VAL_SET_PREFIX=$7
RAW_VAL_SET_INDEX_PATH=$8
RAW_VAL_SET_ANNO_ROOT=$9
MINING_SET_PREFIX=${10}
RAW_MINING_SET_INDEX_PATH=${11}
RAW_MINING_SET_ANNO_ROOT=${12}

C_OFF='\033[0m'
C_RED='\033[0;31m'
C_GREEN='\033[0;32m'
C_YELLOW='\033[0;33m'
C_RED_BOLD='\033[1;31m'
C_GREEN_BOLD='\033[1;32m'
C_YELLOW_BOLD='\033[1;33m'
import() {
    # import training dataset
    _echo_in_color $C_YELLOW "import from master to $TRAINING_SET_PREFIX"
    $MIR_EXE checkout master --root "$MIR_ROOT"
    $MIR_EXE import --root "$MIR_ROOT" \
                    --index-file "$RAW_TRAINING_SET_INDEX_PATH" \
                    --annotation-dir "$RAW_TRAINING_SET_ANNO_ROOT" \
                    --gen-dir "$YMIR_ASSET_LOCATION" \
                    --dataset-name "$TRAINING_SET_PREFIX" \
                    --dst-rev "$TRAINING_SET_PREFIX@$TRAINING_SET_PREFIX"

    # import val dataset
    _echo_in_color $C_YELLOW "import from master to $VAL_SET_PREFIX"
    $MIR_EXE checkout master --root "$MIR_ROOT"
    $MIR_EXE import --root "$MIR_ROOT" \
                    --index-file "$RAW_VAL_SET_INDEX_PATH" \
                    --annotation-dir "$RAW_VAL_SET_ANNO_ROOT" \
                    --gen-dir "$YMIR_ASSET_LOCATION" \
                    --dataset-name "$VAL_SET_PREFIX" \
                    --dst-rev "$VAL_SET_PREFIX@$VAL_SET_PREFIX"

    # import mining dataset
    _echo_in_color $C_YELLOW "import from master to $MINING_SET_PREFIX"
    $MIR_EXE checkout master --root "$MIR_ROOT"
    $MIR_EXE import --root "$MIR_ROOT" \
                    --index-file "$RAW_MINING_SET_INDEX_PATH" \
                    --annotation-dir "$RAW_MINING_SET_ANNO_ROOT" \
                    --gen-dir "$YMIR_ASSET_LOCATION" \
                    --dataset-name "$MINING_SET_PREFIX" \
                    --dst-rev "$MINING_SET_PREFIX@$MINING_SET_PREFIX"

    # first merge: _MERGED_TRAINING_SET_PREFIX-0 = tr:TRAINING_SET_PREFIX + va: VAL_SET_PREFIX
    # _echo_in_color $C_YELLOW "merge from tr:$TRAINING_SET_PREFIX + va:$VAL_SET_PREFIX to $_MERGED_TRAINING_SET_PREFIX-0"
    # $MIR_EXE merge --root $MIR_ROOT \
    #                --src-revs "tr:$TRAINING_SET_PREFIX@$TRAINING_SET_PREFIX;va:$VAL_SET_PREFIX@$VAL_SET_PREFIX" \
    #                --dst-rev "$_MERGED_TRAINING_SET_PREFIX-0@$_MERGED_TRAINING_SET_PREFIX-0" \
    #                -s host
}

post_import_success() {
    _echo_in_color $C_GREEN "$1 success"
    echo "next: run $0 training 0"
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
