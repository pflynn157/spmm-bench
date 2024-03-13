#!/bin/bash
BENCH_NAME="ell"
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
    
    for k in "${k_loop[@]}"
    do
        for O in "${OLEVELS[@]}"
        do
            for t in "${threads[@]}"
            do
                echo "[OMP] ell --k $k --threads $t"
                printf "ell_omp_${O}," >> $CSV_FILE
                $BIN/ell_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[OMP Collapse] ell --k $k --threads $t"
                printf "ell_omp_collapse_${O}," >> $CSV_FILE
                $BIN/ell_omp_collapse_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMP] ell --k $k --threads $t"
                printf "ell_transpose_omp_${O}," >> $CSV_FILE
                $BIN/ell_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMP Collapse] ell --k $k --threads $t"
                printf "ell_transpose_omp_collapse_${O}," >> $CSV_FILE
                $BIN/ell_transpose_omp_collapse_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMPxOMP] ell --k $k --threads $t"
                printf "ell_transpose_omp_omp_${O}," >> $CSV_FILE
                $BIN/ell_transpose_omp_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
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
