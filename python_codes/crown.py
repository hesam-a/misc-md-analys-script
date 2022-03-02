from itertools import islice
import sys
from subprocess import PIPE, run

#adds the prm indecies to a crown ether xyz file 


g = sys.argv[1]
f = open(g,'r')

cmd = run(["head", "-1", g], stdout=PIPE, stderr=PIPE, universal_newlines=True)
#print(cmd.stdout.split()[0])

natoms = int(cmd.stdout.split()[0])
b=['   406     7    19','   406     8    20','   406     9    21','   406    10    22','   407    23    25','   407    24    26','   402     1     8    11    27','   402     2     7    12    28','   402     3    10    13    29','   402     4     9    14    30','   401     7    15    31    32','   401     8    16    33    34','   401     9    17    35    36','   401    10    18    37    38','   403    11    16    39    40','   403    12    15    41    42','   403    13    18    43    44','   403    14    17    45    46','   404     1    23    47    48','   404     2    24    49    50','   404     3    25    51    52','   404     4    26    53    54','   405     5    19    55    56','   405     6    20    57    59','   405     5    21    58    60','   405     6    22    61    62','   408     7','   408     8','   408     9','   408    10','   410    11','   410    11', '   410    12','   410    12','   410    13','   410    13','   410    14','   410    14','   409    15','   409    15','   409    16','   409    16','   409    17','   409    17','   409    18','   409    18','   412    19','   412    19','   412    20','   412    20','   412    21', '   412    21', '   412    22', '   412    22','   411    23', '   411    23','   411    24','   411    25','   411    24','   411    25','   411    26','   411    26','   601','   15','   15']

for line in f:
    if line.strip() == str(natoms):
        a = ''.join(islice(f,0,natoms))
        c=a.splitlines()
        l=open("new_crown.arc","a")
        l.write('   '+line.strip()+"\n")
        counter = 0
        for i in range(natoms):
            counter +=1
            l.write('   '+str("{:>4}".format(counter))+c[i]+b[i]+'\n')
        l.close()
    else:
        pass

f.close()
