import sys
from itertools import islice
from subprocess import PIPE, run
from statistics import mean

# finds the mean value of the side_length of the box from arc file for PBC and volume purposes

g = sys.argv[1]
f = open(g,'r')

cmd = run(["head", "-1", g], stdout=PIPE, stderr=PIPE, universal_newlines=True)
#print(cmd.stdout.split()[0])

natoms = int(cmd.stdout.split()[0])
side_length=[]
for line in f:
    if line.strip() == str(natoms):
        a = ' '.join(islice(f,1))
        side_length.append(float(a.split()[0]))
print(mean(side_length))
f.close()

