import sys
from itertools import islice

# This program generates xyz files of imidazole for ion parameterization from orca package output file

f = open (sys.argv[1], 'r')

for line in f:
    if 'TRAJECTORY STEP' in line:
        # find the coord lines after each sp step
        a = ''.join(islice(f,5,15))

        # split each line 
        b=a.splitlines()

        # find the distance of ion and the binded atom
        b1=b[1].split()

        # convert the distance value from string to float
        c=float(b1[1])

        # round to remove the zeros
        b2=round(c,2)

        # write each line with the binded atom numbers to file 
        g = open(f"Imidazole_Sm2+_0{b2}.txyz", 'w')

        # write the number of atoms and coord lines manually 
        g.write(' 10  # generated by xyzToTxyz, by Hesam A. @ FSU\n')
        g.write('      1 '+b[0]+'   507  \n')
        g.write('      2 '+b[1]+'   262  5  3   \n')
        g.write('      3 '+b[2]+'   263  4  2  8\n')
        g.write('      4 '+b[3]+'   265  6  7  3 \n')
        g.write('      5 '+b[4]+'   260  6 10  2 \n')
        g.write('      6 '+b[5]+'   258  9  5  4 \n')
        g.write('      7 '+b[6]+'   266  4 \n')
        g.write('      8 '+b[7]+'   264  3 \n')
        g.write('      9 '+b[8]+'   259  6 \n')
        g.write('     10 '+b[9]+'   261  5 \n')
        g.close()
    else:
        pass
