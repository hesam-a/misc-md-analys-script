from itertools import islice
import sys

# extracts the coordinates of a ligand/molecule out of arc/trajectory file (from the beginning)

g = sys.argv[1]
arcReader = open(g,'r')

cmd = run(["head", "-1", g], stdout=PIPE, stderr=PIPE, universal_newlines=True)
#print(cmd.stdout.split()[0])

natoms = int(cmd.stdout.split()[0])

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
