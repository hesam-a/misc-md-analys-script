import os
import subprocess
import sys
from shutil import copyfile

# creates the required directories/steps for an MD sim and copies xyz and prm and key files

#python mdsimsprep.py *.key amoeba.prm

keyfile=sys.argv[1]
prmfile=sys.argv[2]
directname = sys.argv[3]
foldlist=['heat','eq','prod']

mdsimpath=os.getcwd()

if not os.path.isdir(directname):
    os.mkdir(directname)
else:
    pass
os.chdir(directname)

for i in foldlist:
    if not os.path.isdir(i):
        os.mkdir(i)
    else:
        pass
    os.chdir(i) 
    newfoldpath=os.getcwd()
    copyfile(mdsimpath+'/'+keyfile,newfoldpath+'/'+keyfile)
    copyfile(mdsimpath+'/'+prmfile,newfoldpath+'/'+prmfile)
    os.chdir('..')
