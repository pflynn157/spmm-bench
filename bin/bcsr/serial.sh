#!/bin/bash
BENCH_NAME="bcsr_serial"
ARCH_ID=$1

source bin/config.sh
source bin/lib.sh
setup

##
## Our run function
##
function run() {
    NAME=$1
    CSV_FILE=report/csv/$1_"$BENCH_NAME"_"$ARCH_ID".csv
    init_csv $CSV_FILE
    
    for O in "${OLEVELS[@]}"
    do
        for k in "${k_loop[@]}"
        do
            for b in "${blocks[@]}"
            do
                echo "[Serial] bcsr --k $k ${b}x${b}"
                printf "BCSR Serial,${O}," >> $CSV_FILE
                $BIN/bcsr_serial_${O} data/$NAME.mtx --iters $iters --k $k --block $b >> $CSV_FILE
            done
        done
    done
}

##
## Run the benchmark on all available data
##
for mtx in data/*.mtx
do
    input_mtx=`basename $mtx .mtx`
    
    echo ""
    echo "-----------$input_mtx--------------------"
    run $input_mtx
done

