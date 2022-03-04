from itertools import islice
import sys

# this program generates trajectory of ONLY molecule(s) of your interest (excluding the solvent) from md trajectory file 
#useful for conformational analysis or use in cpptraj of Amber Tools

arcReader = open(sys.argv[1],'r')
natoms = int(sys.argv[2])
outfile = sys.argv[3]


counter=0
for line in arcReader:
    if ' 90.000000 ' in line:
        a = ''.join(islice(arcReader,0,natoms))
        c=a.splitlines()
        g=open(outfile,"a")
#        g = open(f"dch-18cr_frame-0{counter}.txyz", 'w')
        g.write('    '+str(natoms)+' \n')
        for i in range(natoms):
            g.write(''+c[i]+'\n')
        g.close()
        counter += 1    
    else:
        pass
