from plot import *

matrix = [
    "2cubes_sphere",
    "af23560",
    "bcsstk13",
    "bcsstk17",
    "cant",
    "cop20k_A",
    "crankseg_2",
    "dw4096",
    "nd24k",
    "pdb1HYS",
    "rma10",
    "shallow_water1",
    "torso1",
    "x104",
]

###############################################################
## Arm
###############################################################

# COO
#frame = create_data(matrix, ["coo"], ["serial", "omp"], ["arm"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "COO- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_coo_arm")

# CSR
#frame = create_data(matrix, ["csr"], ["serial", "omp"], ["arm"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "CSR- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_csr_arm")

# ELL
#frame = create_data(matrix, ["ell"], ["serial", "omp"], ["arm"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "ELL- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_ell_arm")

# BCSR
#frame = create_data(matrix, ["bcsr"], ["serial", "omp"], ["arm"], filter_eq=[("Block Row", 4), ("Block Col", 4)])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "BCSR- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_bcsr_arm")

## Arm
frame = create_data(matrix, ["coo"], ["omp"], ["arm"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "COO- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_coo_arm")

frame = create_data(matrix, ["csr"], ["omp"], ["arm"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "CSR- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_csr_arm")

frame = create_data(matrix, ["ell"], ["omp"], ["arm"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "ELL- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_ell_arm")

frame = create_data(matrix, ["bcsr"], ["omp"], ["arm"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "BCSR- Serial- K Study (Arm)", "MFLOPS", "Matrix", "Name", output= "study4_bcsr_arm")


###############################################################
## x86
###############################################################

# COO
#frame = create_data(matrix, ["coo"], ["serial", "omp"], ["intel"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "COO- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_coo_intel")

# CSR
#frame = create_data(matrix, ["csr"], ["serial", "omp"], ["intel"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "CSR- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_csr_intel")

# ELL
#frame = create_data(matrix, ["ell"], ["serial", "omp"], ["intel"])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "ELL- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_ell_intel")

# BCSR
#frame = create_data(matrix, ["bcsr"], ["serial", "omp"], ["intel"], filter_eq=[("Block Row", 4), ("Block Col", 4)])
#frame = change_names(frame, "K-Bound", " -k ")
#plot_grouped_bar(frame, "BCSR- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_bcsr_intel")


## x86
frame = create_data(matrix, ["coo"], ["omp"], ["intel"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "COO- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_coo_intel")

frame = create_data(matrix, ["csr"], ["omp"], ["intel"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "CSR- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_csr_intel")

frame = create_data(matrix, ["ell"], ["omp"], ["intel"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "ELL- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_ell_intel")

frame = create_data(matrix, ["bcsr"], ["omp"], ["intel"])
frame = change_names(frame, "K-Bound", " -k ")
plot_grouped_bar(frame, "BCSR- Serial- K Study (x86)", "MFLOPS", "Matrix", "Name", output= "study4_bcsr_intel")

