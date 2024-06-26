#!/bin/bash
BENCH_NAME="coo_gpu"
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
            echo "[GPU] coo --k $k"
            printf "COO GPU,${O}," >> $CSV_FILE
            TEXT=""
            #TEXT=`$BIN/coo_omp_gpu_${O} data/$NAME.mtx --iters $iters --k $k`
            while true; do
                TEXT=$($BIN/coo_omp_gpu_${O} data/$NAME.mtx --iters $iters --k $k)
                if [ $? -eq 0 ]; then
                    break
                fi
            done
            echo $TEXT >> $CSV_FILE
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

