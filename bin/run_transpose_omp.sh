#!/bin/bash
BENCH_NAME="transpose_omp"
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
    
    for t in "${threads[@]}"
    do
        for k in "${k_loop[@]}"
        do
            for O in "${OLEVELS[@]}"
            do
                echo "[Transpose OMP] coo --k $k --threads $t"
                printf "coo_transpose_omp_${O}," >> $CSV_FILE
                $BIN/coo_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMP] csr --k $k --threads $t"
                printf "csr_transpose_omp_${O}," >> $CSV_FILE
                $BIN/csr_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                echo "[Transpose OMP] ell --k $k --threads $t"
                printf "ell_transpose_omp_${O}," >> $CSV_FILE
                $BIN/ell_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --threads $t >> $CSV_FILE
                
                for b in "${blocks[@]}"
                do
                    echo "[Transpose OMP] bcsr --k $k ${b}x${b} --threads $t"
                    printf "bcsr_transpose_omp_${O}," >> $CSV_FILE
                    $BIN/bcsr_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --block $b --threads $t >> $CSV_FILE
                    
                    echo "[Transpose OMP] bell --k $k ${b} --threads $t"
                    printf "bell_transpose_omp_${O}," >> $CSV_FILE
                    $BIN/bell_transpose_omp_${O} data/$NAME.mtx --iters $iters --k $k --block $b --threads $t >> $CSV_FILE
                done
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

