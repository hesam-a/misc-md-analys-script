import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#plots the error bars of bond length with three-sigma std dev

syn_thf=[2.745,2.755,2.785,2.735]
syn_aceto=[2.725,2.705,2.725,2.705]
anti_thf=[2.745,2.745,2.745,2.715]
trans_aceto=[2.715,2.675,2.695,2.695]
trans_thf=[2.725,2.725,2.705,2.715]


syn_thf_mean     = np.mean(syn_thf)
syn_aceto_mean   = np.mean(syn_aceto)
anti_thf_mean    = np.mean(anti_thf)
trans_aceto_mean = np.mean(trans_aceto) 
trans_thf_mean   = np.mean(trans_thf)

print('syn_thf_mean    : ',    syn_thf_mean)
print('syn_aceto_mean  : ',  syn_aceto_mean)
print('anti_thf_mean   : ',   anti_thf_mean)
print('trans_aceto_mean: ',trans_aceto_mean)
print('trans_thf_mean  : ',  trans_thf_mean)

syn_thf_stdev     = 3*np.std(syn_thf)
syn_aceto_stdev   = 3*np.std(syn_aceto)
anti_thf_stdev    = 3*np.std(anti_thf)
trans_aceto_stdev = 3*np.std(trans_aceto) 
trans_thf_stdev   = 3*np.std(trans_thf)


y_ax  = [syn_thf_mean,syn_aceto_mean,anti_thf_mean,trans_aceto_mean,trans_thf_mean]
x_ax  = ['CSC\n THF','CSC\n MeCN','CAC\n THF','TAT\n MeCN','TAT\n THF']
x_err = [syn_thf_stdev,syn_aceto_stdev,anti_thf_stdev,trans_aceto_stdev,trans_thf_stdev]

##plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True

font = FontProperties()
font.set_weight('bold')
#font.set_size('13')

fig,ax = plt.subplots()
#ax = plt.gca()#add_axes(left, bottom, width, height)
bars=ax.bar(x_ax,y_ax,yerr=x_err,width=0.5,color='red',ec='black',ecolor='black',capsize=4)
ax.bar_label(bars, labels=['±%.2f' % e for e in x_err],
             padding=8, color='black', fontsize=14,fontweight="bold")
ax.spines['top'].set_linewidth(2)
ax.set_title('(Sm$^{2+}$- O) interaction distances ($ \AA$)', fontsize=13, fontweight="bold")#$Cl^-$/$Br^-$/$I^-$
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
#plt.xlabel(labelpad=12, fontsize=10, fontweight="bold")
#ax.set_xticks(x_ax,font)
plt.ylabel('Interaction distances ($ \AA$)', labelpad=12, fontsize=15, fontweight="bold")
#plt.xlim([2,4])
plt.ylim([2.5,3])
plt.xticks(fontsize=13, fontweight="bold")
plt.yticks(fontsize=13, fontweight="bold")
#plt.legend(frameon=False, prop=font)

plt.savefig("Sm-O_BL.png",
            dpi=200,
#            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True,
            facecolor ="w",
            edgecolor ='w',
            orientation ='landscape')
plt.show()
