#include <omp.h>

#include "matrix.h"

//
// The calculation algorithm for the current format
//
double Matrix::calculate() {
    double start = getTime();
    
    // Transpose
    double* B_trans = new double[rows * cols];

    for (size_t i = 0; i < rows; ++i) {
      for (size_t j = 0; j < cols; ++j) {
        B_trans[j * rows + i] = B[i*cols+j];
      }
    }
    
    size_t i = 0;
    size_t _rows = rows;
    size_t _cols = cols;
    size_t _num_cols = num_cols;
    size_t _k_bound = k_bound;
    uint64_t *_colidx = colidx;
    double *_values = values;
    double *_C = C;
    
    #pragma omp target teams distribute parallel for \
        map(to: _rows, _cols, _num_cols, _k_bound, _colidx[0:rows*num_cols], _values[0:rows*num_cols], B_trans[0:rows*cols]) \
        map(tofrom: _C[0:rows*cols])
    for (i = 0; i<rows; i++) {
        size_t _i = i;
        for (uint64_t n1 = 0; n1<_num_cols; n1++) {
            uint64_t p = _i * _num_cols + n1;
            uint64_t j = _colidx[p];
            for (uint64_t k = 0; k<_k_bound; k++) {
                _C[_i*_cols+j] += _values[p] * B_trans[j*_cols+k];
            }
        }
    }
    
    C = _C;
    
    double end = getTime();
    return (double)(end-start);
}
