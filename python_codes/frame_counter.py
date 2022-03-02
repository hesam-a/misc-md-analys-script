import os
import subprocess

# frame/line counter for BAR free energy sims to keep track of each baby simulations

HostGuestSimPath = '/home/hesam/Documents/projects/md_clacs/bar_dch18-cis-syn/test2/ProteinLigandSim/'
GuestSimPath =  '/home/hesam/Documents/projects/md_clacs/bar_dch18-cis-syn/test2/LigandSim/'
ParentDir = '/home/hesam/Documents/projects/md_clacs/bar_dch18-cis-syn/test2/'
solvvdw= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,.97,.93,.9,.87,.83,.8,.77,.73,.7,.68,.65,.62,.60,.55,.5,.4,0]
solvestat=[1,.95,.9,.85,.8,.75,.7,.65,.6,.55,.5,.45,.4,.35,.3,.25,.2,.15,.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

HGsims=False
Gsims=True


if HGsims:
    for i in range(len(solvvdw)):
        os.chdir(HostGuestSimPath)
        vdwlamb=solvvdw[i]
        elelamb=solvestat[i]
        subHG="HostGuestSimPath%s_%s"%(elelamb,vdwlamb)
        subdir = os.chdir(os.getcwd()+'/'+subHG+'/')
        direc_files=os.listdir(os.getcwd())
        for fil in direc_files:
            if '.arc' in fil:
                cmd = subprocess.run(["wc", "-l", "thfdchdy2.arc"], stdout=subprocess.PIPE)
                print(cmd.stdout,"          ",subHG)
            else:
                pass
        os.chdir('..')

if Gsims:
    os.chdir(GuestSimPath)
    subdir = sorted(os.listdir(os.getcwd()),reverse=True)
    for direc in subdir:
        os.chdir(os.getcwd()+'/'+direc+'/')
        direc_files=os.listdir(os.getcwd())
        for fil in direc_files:
            if '.arc' in fil:
                cmd = subprocess.run(["wc", "-l", "thfdy2.arc"], stdout=subprocess.PIPE)
                print(cmd.stdout,"          ",direc)
                print('')
            else:
                pass
        os.chdir('..')
