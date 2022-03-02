import sys
from itertools import islice
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# after analyzing the energies of a trajectory/molecule outputs the energy components in a csv file and plot them.

f = open(sys.argv[1],'r')


def energy_comp(x):
    g = open("energy_data.csv",'a')
    g.write("frame #, potential energy, torsion,vdW, electrostatics \n")
    frame_counter=[]
    potential = []
    torsion = []
    vdw = []
    electrostat = [] 

    for line in x:
        if "Analysis for Archive Structure" in line:
            data = ''.join(islice(x,0,14))
            splt = data.splitlines()
            elec = float(splt[12].split()[2])+float(splt[13].split()[1])
            frame_counter.append(float(line.split()[5]))
            potential.append(float(splt[3].split()[4]))
            torsion.append(float(splt[10].split()[2]))
            vdw.append(float(splt[11].split()[3]))
            electrostat.append(float(elec))
            g.write(line.split()[5]+','+splt[3].split()[4]+','+splt[10].split()[2]+','+splt[11].split()[3]+','+str(elec)+'\n')
    g.close()

    return frame_counter, potential, torsion,vdw, electrostat

frame,potential, torsion, vdw, elec  = energy_comp(f)


plt.rcParams["figure.autolayout"] = True


font = FontProperties()
font.set_weight('bold')

fig,ax = plt.subplots()
#ax.plot(frame,potential, linewidth = '1', color='#f400ff', linestyle='solid', label='Total Potential Energy')#,linestyle='dotted') #ff0000  'o',
ax.plot(frame,torsion,   linewidth = '1', color='#0700ff', linestyle='solid', label='Torsion Energy')#,linestyle='dotted')#0700ff           'v',
ax.plot(frame,vdw,       linewidth = '1', color='#ff0000', linestyle='solid', label='vdW')#linestyle='dotted')    #0f7400                   '+',
ax.plot(frame,elec,      linewidth = '1', color='#f400ff', linestyle='solid', label='Electrostatics')#linestyle='dotted')    #0f7400        '*'
#ax = plt.gca()#add_axes(left, bottom, width, height)
ax.spines['top'].set_linewidth(2)
ax.set_title('SmI$_2$- cis-syn-cis in MeCN', fontsize=13, fontweight="bold")#$Cl^-$/$Br^-$/$I^-$
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.xlabel("MD Frame Number", labelpad=12, fontsize=14, fontweight="bold")
plt.ylabel("Potential Energy Comp. (Kcal/mol)", labelpad=12, fontsize=14, fontweight="bold")
#plt.xlim([0,10])
plt.ylim([-600,300])
plt.xticks(fontsize=13, fontweight="bold")
plt.yticks(fontsize=13, fontweight="bold")

plt.legend(frameon=False, prop=font, loc='best')

plt.savefig("SmI2_thf_energy_comp.png",
            dpi=200,
#            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True,
            facecolor ="w",
            edgecolor ='w',
            orientation ='landscape')
plt.show()
f.close()
