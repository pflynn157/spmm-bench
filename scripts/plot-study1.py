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

fmt = [ "coo", "csr", "ell", "bcsr" ]

########################################################
## Arm
########################################################

## Study 1- serial- all formats
frame = create_data(matrix, fmt, ["serial"], ["arm"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
plot_grouped_bar(frame, "Serial- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_serial_arm")

## Study 1- parallel- all formats
frame = create_data(matrix, fmt, ["omp"], ["arm"], filter_eq=[("K-Bound", 128), ("Threads", 32)])
plot_grouped_bar(frame, "Parallel- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_omp_arm")

## Study 1- GPU- all formats
frame = create_data(matrix, fmt, ["gpu"], ["arm"], filter_eq=[("K-Bound", 128)])
plot_grouped_bar(frame, "GPU- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_gpu_arm")


# New study
## Study 1- serial- all formats
frame = create_data(matrix, fmt, ["serial"], ["arm2"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
plot_grouped_bar(frame, "Serial- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_1_serial_arm")

frame = create_data(matrix, fmt, ["serial"], ["arm", "arm2"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
frame = change_names(frame, "Archs", " ", True)
plot_grouped_bar(frame, "Serial- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_2_serial_arm")

## Study 1- parallel- all formats
frame = create_data(matrix, fmt, ["omp"], ["arm2"], filter_eq=[("K-Bound", 128), ("Threads", 32)])
plot_grouped_bar(frame, "Parallel- All Types (Arm)", "MFLOPS", "Matrix", "Name", output= "study1_1_omp_arm")


########################################################
## x86
########################################################

## Study 1- serial- all formats
frame = create_data(matrix, fmt, ["serial"], ["intel"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
plot_grouped_bar(frame, "Serial- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_serial_intel")

## Study 1- parallel- all formats
frame = create_data(matrix, fmt, ["omp"], ["intel"], filter_eq=[("K-Bound", 128), ("Threads", 32)])
plot_grouped_bar(frame, "Parallel- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_omp_intel")


# New study
## Study 1- serial- all formats
frame = create_data(matrix, fmt, ["serial"], ["intel2"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
plot_grouped_bar(frame, "Serial- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_1_serial_intel")

frame = create_data(matrix, fmt, ["serial"], ["intel", "intel2"], filter_eq=[("K-Bound", 128), ("Block Row", 4), ("Block Col", 4)])
frame = change_names(frame, "Archs", " ", True)
plot_grouped_bar(frame, "Serial- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_2_serial_intel")

## Study 1- parallel- all formats
frame = create_data(matrix, fmt, ["omp"], ["intel2"], filter_eq=[("K-Bound", 128), ("Threads", 32)])
plot_grouped_bar(frame, "Parallel- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_1_omp_intel")


## Study 1- GPU- all formats
matrix = [
    #"2cubes_sphere",
    "af23560",
    "bcsstk13",
    "bcsstk17",
    #"cant",
    #"cop20k_A",
    #"crankseg_2",
    "dw4096",
    #"nd24k",
    "pdb1HYS",
    "rma10",
    #"shallow_water1",
    #"torso1",
    #"x104",
]

frame = create_data(matrix, fmt, ["gpu"], ["intel"], filter_eq=[("K-Bound", 128)])
plot_grouped_bar(frame, "GPU- All Types (x86)", "MFLOPS", "Matrix", "Name", output= "study1_gpu_intel")

