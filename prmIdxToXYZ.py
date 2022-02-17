from itertools import islice
import sys
from subprocess import PIPE, run

# reads the parameter indices of one frame of an arc file and adds the indices to the xyz file


g = sys.argv[1];
arc = open(g,'r');
f = sys.argv[2];
xyz = open(f,'r');


cmd_arc = run(["head", "-1", g], stdout=PIPE, stderr=PIPE, universal_newlines=True);
natoms_arc = int(cmd_arc.stdout.split()[0]);

cmd_xyz = run(["head", "-1", f], stdout=PIPE, stderr=PIPE, universal_newlines=True);
natoms_xyz = int(cmd_xyz.stdout.split()[0]);

prm_index=[];

for line in arc:
    if line.strip() == str(natoms_arc):
        a = ''.join(islice(arc,1,natoms_xyz+1));
        c=a.splitlines();
        for i in c:
            prm="";
            a=i.split()[5:];
            for j in a:
                prm += j+"   ";
            prm_index.append(prm);
    break

print(prm_index);


for line in xyz:
    if line.strip() == str(natoms_xyz):
        a = ''.join(islice(xyz,0,natoms_xyz));
        c=a.splitlines();
        l=open("new_crown.arc","a");
        l.write('   '+line.strip()+"\n");
        counter = 0;
        for i in range(natoms_xyz):
            counter +=1;
            l.write('     '+str("{:>3}".format(counter))+c[i]+"   "+prm_index[i]+'\n');
        l.close();
    else:
        pass

arc.close();
xyz.close();
