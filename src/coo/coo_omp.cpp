#include "matrix.h"

double Matrix::calculate() {
    double start = getTime();
    
    #pragma omp parallel for
    for (size_t arg0 = 0; arg0<coo->nnz; arg0++) {
        size_t i = coo_rows[arg0];
        size_t j = coo_cols[arg0];
        double val = coo_vals[arg0];
        for (size_t k = 0; k<cols; k++) {
            C[i*cols+j] += val * B[k*cols+j];
        }
    }
    
    double end = getTime();
    return (double)(end-start);
}

