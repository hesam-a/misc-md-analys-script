import subprocess
from os import path
import os

# keeps track of generated bar files, if generated twice with "bar_2" attribution, can modify or delete.

global Guestsimpath
global HostGuestsimpath
global solvdw
global solvestat
global HostGuestbar
global Guestbar


Guestsimpath='/home/hesam/Documents/projects/md_clacs/dy2+/bar_cis-syn-cis/GuestSim/'
HostGuestsimpath='/home/hesam/Documents/projects/md_clacs/dy2+/bar_cis-syn-cis/HostGuestSim/'

solvvdw= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,.97,.93,.9,.87,.83,.8,.77,.73,.7,.68,.65,.62,.60,.55,.5,.4,0]
solvestat=[1,.95,.9,.85,.8,.75,.7,.65,.6,.55,.5,.45,.4,.35,.3,.25,.2,.15,.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

HostGuestbar=True
Guestbar=True


def bar_2_changer():
    if HostGuestbar:
        os.chdir(HostGuestsimpath)
        for i in range(len(solvestat)-1):
            secondelelamb=solvestat[i]
            secondvdwlamb=solvvdw[i]
            secondfoldname=HostGuestsimpath+"HostGuestSim%s_%s"%(secondelelamb,secondvdwlamb)
            os.chdir(secondfoldname)
            barfile = 'thfdchdy2.bar'
            if path.exists(barfile):
                os.remove(barfile)
                print("In %s    FOUND a bar file"%(secondfoldname))
            else:
                print("In %s    did NOT find a bar file"%(secondfoldname))
                pass
        os.chdir('..')
    if Guestbar:
        os.chdir(Guestsimpath)
        for i in range(len(solvestat)-1):
            secondelelamb=solvestat[i]
            secondvdwlamb=solvvdw[i]
            secondfoldname=Guestsimpath+"GuestSim%s_%s"%(secondelelamb,secondvdwlamb)
            os.chdir(secondfoldname)
            barfile = 'thfdy2.bar'
            if path.exists(barfile):
                os.remove(barfile)
                print("In %s    FOUND a bar file"%(secondfoldname))
            else:
                print("In %s    did NOT find a bar file"%(secondfoldname))
                pass


def bar_2_modifier():
    if HostGuestbar:
        os.chdir(HostGuestsimpath)
        for i in range(len(solvestat)-1): 
            secondelelamb=solvestat[i]
            secondvdwlamb=solvvdw[i]
            secondfoldname=HostGuestsimpath+"HostGuestSim%s_%s"%(secondelelamb,secondvdwlamb)
            os.chdir(secondfoldname)
            barfile = 'thfdchdy2.bar'
            newbarfile = 'thfdchdy2_old.bar'
            if path.exists(barfile):
                barfilepath=secondfoldname+'/'+barfile
                newbarfilepath=secondfoldname+'/'+newbarfile
                os.rename(barfilepath,newbarfilepath)
                print("In %s    FOUND a bar file"%(secondfoldname))
            else:
                print("In %s    did NOT find a bar file"%(secondfoldname))
                pass
        os.chdir('..')
    if Guestbar:
        os.chdir(Guestsimpath)
        for i in range(len(solvestat)-1): 
            secondelelamb=solvestat[i]
            secondvdwlamb=solvvdw[i]
            secondfoldname=Guestsimpath+"GuestSim%s_%s"%(secondelelamb,secondvdwlamb)
            os.chdir(secondfoldname)
            barfile = 'thfdy2.bar'
            newbarfile = 'thfdy2_old.bar'
            if path.exists(barfile):
                barfilepath=secondfoldname+'/'+barfile
                newbarfilepath=secondfoldname+'/'+newbarfile
                os.rename(barfilepath,newbarfilepath)
                print("In %s    FOUND a bar file"%(secondfoldname))
            else:
                print("In %s    did NOT find a bar file"%(secondfoldname))
                pass

#bar_2_modifier()
bar_2_changer()
