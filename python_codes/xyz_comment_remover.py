import sys
from itertools import islice
from subprocess import PIPE, run

# generates vmd-readable txyz files

g = sys.argv[1]
f = open(g,'r')

cmd = run(["head", "-1", g], stdout=PIPE, stderr=PIPE, universal_newlines=True)
#print(cmd.stdout.split()[0])

natoms = int(cmd.stdout.split()[0])

    
for line in f:
    if line.strip() == str(natoms):
        b = '   '.join(islice(f,1))
        a = ''.join(islice(f,0,natoms))
        g=open("new.arc","a")
        g.write('     '+line.strip()+'       '+b)
        c=a.splitlines()
        for i in range(natoms):
            g.write('    '+c[i]+'\n')
        g.close()
    else:
        pass
f.close()
