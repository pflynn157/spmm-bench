#!/bin/bash

function generate() {
# Input CSV file
csv_file="$1"

# Output image file
output_image="$2"

# Plotting script for gnuplot
gnuplot_script=$(cat <<EOF
set datafile separator ","
set terminal pngcairo enhanced font 'arial,10' size 1600,1200
set output "${output_image}"
set title "$3"
set ylabel "$4"
set xlabel "Executable"
set style fill solid
set boxwidth 0.5
set xtics rotate by -45
plot "${csv_file}" using 2:xtic(1) with boxes title "AvgExecutionTime"
EOF
)


# Create and execute the gnuplot script
echo "${gnuplot_script}" | gnuplot

echo "Bar figure generated: ${output_image}"
}

generate "bcsstk17_csr_bcsr_arm-avg-run.csv" "bcsstk17_csr_bcsr_arm-avg-run.png" \
    "BCSSTK17 CSRxBCSR- Average Runtimes" "Average Runtimes"
generate "bcsstk17_csr_bcsr_arm-total.csv" "bcsstk17_csr_bcsr_arm_total.png" \
    "BCSSTK17 CSRxBCSR- Total Runtimes" "Total Runtimes"

