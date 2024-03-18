#!/bin/bash
BENCH_NAME="csr"
ARCH_ID=$1

source bin/config.sh
source bin/lib.sh
setup

##
## Our run function
##
function run() {
    NAME=$1
    CSV_FILE=report/csv/$1_"$BENCH_NAME"_"$ARCH_ID"_collapse.csv
    init_csv $CSV_FILE
    
    for k in "${k_loop[@]}"
    do
        for O in "${OLEVELS[@]}"
        do
            for t in "${threads[@]}"
            do
                echo "[Transpose OMP] csr --k $k --threads $t"
                printf "csr_transpose_omp_${O}," >> $CSV_FILE
                $BIN/csr_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMP Collapse] csr --k $k --threads $t"
                printf "csr_transpose_omp_collapse_${O}," >> $CSV_FILE
                $BIN/csr_transpose_omp_collapse_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMPxOMP] csr --k $k --threads $t"
                printf "csr_transpose_omp_omp_${O}," >> $CSV_FILE
                $BIN/csr_transpose_omp_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
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
    run $input_mtx
done
