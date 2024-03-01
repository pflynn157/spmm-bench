#include <omp.h>

#include "matrix.h"

//
// The calculation algorithm for the current format
//
double Matrix::calculate() {
    if (threads != -1) omp_set_num_threads(threads);
    
    double start = getTime();
    
    // Transpose
    double* B_trans = new double[rows * cols];

    for (size_t i = 0; i < rows; ++i) {
      for (size_t j = 0; j < cols; ++j) {
        B_trans[j * rows + i] = B[i*cols+j];
      }
    }
    
    #pragma omp parallel for collapse(2)
    for (uint64_t i = 0; i<rows; i++) {
        for (uint64_t p = rowptr[i]; p<rowptr[i+1]; p++) {
            uint64_t j = colidx[p];
            uint64_t val = values[p];
            for (uint64_t k = 0; k<k_bound; k++) {
                C[i*cols+j] += val * B_trans[j*cols+k];
            }
        }
    }
    
    double end = getTime();
    return (double)(end-start);
}
