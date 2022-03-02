import sys
from itertools import islice
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator
import numpy as np
#from matplotlib import rc


# plots the PES curve 

qm = open(sys.argv[1],'r')
mm = open(sys.argv[2],'r')
molecule = sys.argv[3]
point_num1 = int(sys.argv[4])
point_num2 = int(sys.argv[5])

f = qm.readlines()
g = mm.readlines()
points=[]
qm_data=[]
mm_data=[]

if molecule =='acet':
    for i in range(point_num1,point_num2,1):
        mm_data.append(float(g[i].split()[5].strip()))
        points.append(float(g[i].split()[0][20:23]))
elif molecule =='imid':
    for i in range(point_num1,point_num2,1):
        mm_data.append(float(g[i].split()[5].strip()))
        points.append(float(g[i].split()[0][15:18]))
elif molecule =='wat':
    for i in range(point_num1,point_num2,1):
        mm_data.append(float(g[i].split()[5].strip()))
        points.append(float(g[i].split()[0][16:19]))

for i in range(point_num1,point_num2,1):
    qm_data.append(float(f[i].strip()))

print(points)
print(qm_data)
print(mm_data)

#plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True

#rc('text', usetex=True)

font = FontProperties()
font.set_weight('bold')

fig,ax = plt.subplots()

ax.plot(points,qm_data,'v', linewidth = '2',linestyle='solid', color='#e30000', label="CCSD(T)")
ax.plot(points,mm_data,'o', linewidth = '2',linestyle='solid', color='#1300ff', label='AMOEBA')

#ax = plt.gca()#add_axes(left, bottom, width, height)
#ax.set_title("(PES of Sm$^{2+}$-O in Acetamide ", fontsize=13, fontweight="bold")#$Cl^-$/$Br^-$/$I^-$
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.xlabel("Dy$^{2+}$- O Distance ($ \AA$)", labelpad=15, fontsize=15, fontweight="bold")
plt.ylabel("Interaction Energy (Kcal/mol)", labelpad=15, fontsize=15, fontweight="bold")
plt.xlim([points[0]-0.5,(points[-1]+0.5)])
#plt.ylim([-150,150])
plt.xticks(fontsize=13, fontweight="bold")
plt.yticks(fontsize=13, fontweight="bold")
plt.legend(frameon=False, prop=font)

plt.savefig("Dy2-"+molecule+".png",
            dpi=200,
#            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True,
            facecolor ="w",
            edgecolor ='w',
            orientation ='landscape')
plt.show()

qm.close()
mm.close()
