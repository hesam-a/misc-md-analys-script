from itertools import islice
import sys

# extracts the coordinates of a ligand/molecule out of arc/trajectory file (from the beginning)

arcReader = open(sys.argv[1],'r')
natoms = int(sys.argv[2])

counter=0
for line in arcReader:
    if ' 90.000000 ' in line:
        a = ''.join(islice(arcReader,0,natoms))
        c=a.splitlines()
        g = open(f"dch-18cr_frame-0{counter}.txyz", 'w')
        g.write('    '+str(natoms)+' \n')
        for i in range(natoms):
            g.write(''+c[i]+'\n')
        g.close()
        counter += 1    
    else:
        pass
