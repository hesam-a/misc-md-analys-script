from itertools import islice
import sys

# adds box dimensions of traj file generated from xyz_comment_remover.py to the line after # of atoms (vmd-readable to the orginal tinker xyz) 

f = open(sys.argv[1], 'r')

natoms=int(sys.argv[2])

for line in f:
    if '  '+str(natoms)+'  ' in line and '  90.00000' in line:
        b=line.split() 
        a = ''.join(islice(f,0,natoms))
        g=open("new_txyz.arc","a")
        g.write('     '+str(natoms)+'\n')
        g.write('       '+b[1]+'   '+b[2]+'   '+b[3]+'   '+b[4]+'   '+b[5]+'   '+b[6]+'\n')
        c=a.splitlines()
        for i in range(natoms):
            g.write('    '+c[i]+'\n')
        
        g.close()
    else:
        pass

f.close()
