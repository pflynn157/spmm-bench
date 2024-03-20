

##
## The S-ELL structures
##
dim = 8
rowptr = [ 0, 5, 10, 12, 14, 15, 16, 17, 18 ]
colidx = [
    0, 1, 2, 5, 7,
    0, 1, 2, 0, 0,
    2, 7,
    0, 0,
    0,
    0,
    6,
    0,
]
vals = [
    5, 2, 4, 2, 5,
    3, 7, 2, 0, 0,
    7, 5,
    0, 0,
    0,
    8,
    3,
    0,
]

print("colidx: ", colidx)
print("values: ", vals)
exit(0)

##
## The algorithm
##
# Iterate over rows
for n1 in range(dim):
    for n2 in range(rowptr[n1], rowptr[n1+1]):
        print(n1, " ", n2, " -> ", vals[n2])
    print("---")
