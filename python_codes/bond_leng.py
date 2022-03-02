import os, sys
from itertools import islice

#find the mean bond lengths of two atoms from ORCA output

f = open(sys.argv[1], 'r')
atom1 = sys.argv[2]
atom2 = sys.argv[3]

counter = 0
bond_leng = 0.0

for line in f:
    if 'HURRAY' in line:
        a = ''.join(islice(f,5,1000))
        for line in a.splitlines():
            if "B(" in line and atom1+" " in line and atom2+" " in line:
                counter +=1
                bond_leng += float(line.split()[4])

print(" ")
print(f"   The average bond length is {round(bond_leng/counter,2)} Angstrom")
print(" ")
