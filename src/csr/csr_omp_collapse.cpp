#include <omp.h>

#include "matrix.h"

//
// The calculation algorithm for the current format
//
double Matrix::calculate() {
    if (threads != -1) omp_set_num_threads(threads);
    
    double start = getTime();
    
    #pragma omp parallel for collapse(2)
    for (size_t i = 0; i<rows; i++) {
        for (uint64_t p = rowptr[i]; p<rowptr[i+1]; p++) {
            uint64_t j = rowidx[p];
            for (uint64_t k = 0; k<k_bound; k++) {
                C[i*cols+j] += values[p] * B[k*cols+j];
            }
        }
    }
    
    double end = getTime();
    return (double)(end-start);
}

