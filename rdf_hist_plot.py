import sys
from itertools import islice
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#plots the RDF and coordination number (histogram of RDF) curve from VMD RDF 

f = open(sys.argv[1],'r')
g = open(sys.argv[2],'r')
h = open(sys.argv[3],'r')
i = open(sys.argv[4],'r')
j = open(sys.argv[5],'r')
k = open(sys.argv[6],'r')

def rdf(x):
    dist = []
    g_r = []
    file_name = str(sys.argv[1]+".csv")
    l = open(file_name,'a')
    l.write("Distance"+", "+"g(r)"+"\n")

    for line in x:
        if "Counts" in line:
            a = ''.join(islice(x,1,203))
            b = a.splitlines()
            for i in range(202):
                l.write(b[i].split()[2]+', '+b[i].split()[3]+"\n")
                dist.append(float(b[i].split()[2]))
                g_r.append(float(b[i].split()[3]))
            l.close()

    return dist,g_r


def hist(x):
    dist = []
    hist = []
    file_name = str(sys.argv[1]+".csv")
    l = open(file_name,'a')
    l.write("Distance"+", "+"Hist"+"\n")

    for line in x:
        if "norm_hist" in line:
            a = ''.join(islice(x,0,99))
            b = a.splitlines()
            for i in range(99):
                l.write(b[i].split()[1]+', '+b[i].split()[3]+"\n")
                dist.append(float(b[i].split()[1]))
                hist.append(float(b[i].split()[3]))
            l.close()

    return dist,hist

cl_hdist, cl_hist = hist(i)
br_hdist, br_hist = hist(j)
i_hdist, i_hist = hist(k)


cl_dist, cl_gr = rdf(f)
br_dist, br_gr = rdf(g)
i_dist, i_gr = rdf(h)
#print(cl_gr,br_gr,i_gr,sep = "\n")

#plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True


font = FontProperties()
font.set_weight('bold')

fig,ax = plt.subplots()
ax.plot(cl_dist,cl_gr, 'o',linewidth = '1', color='#f400ff', linestyle='solid',label="EuCl$_2$ - O")#,linestyle='dotted') #ff0000
ax.plot(cl_dist,br_gr, 'v',linewidth = '1', color='#0700ff', linestyle='solid',label='EuBr$_2$ - O')#,linestyle='dotted')#0700ff
ax.plot(cl_dist,i_gr, '+', linewidth = '1', color='#ff5e00',  linestyle='solid',label='EuI$_2$ - O')#linestyle='dotted')    #0f7400
#ax = plt.gca()#add_axes(left, bottom, width, height)
ax.spines['top'].set_linewidth(2)
ax.set_title('(Eu$^{2+}$- O) of cis-syn-cis in THF', fontsize=13, fontweight="bold")#$Cl^-$/$Br^-$/$I^-$
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
#plt.xlabel("Eu$^{2+}$- Cl$^-$/Br$^-$/I$^-$ "+r"($ \AA$)", labelpad=12, fontsize=15, fontweight="bold")
plt.xlabel("Eu$^{2+}$- O "+r"($ \AA$)", labelpad=12, fontsize=15, fontweight="bold")
plt.ylabel("g(r)", labelpad=12, fontsize=15, fontweight="bold")
plt.xlim([0,10])
plt.ylim([-0.5,30])
plt.xticks(fontsize=13, fontweight="bold")
plt.yticks(fontsize=13, fontweight="bold")

ax2 = ax.twinx()
ax2.plot(cl_hdist,cl_hist,'o', linewidth = '1', color='#f400ff', linestyle='solid',label="EuCl$_2$- O")#,linestyle='solid') #label="Eu$^{2+}$- Cl$^-$")
ax2.plot(cl_hdist,br_hist,'v', linewidth = '1', color='#0700ff', linestyle='solid',label='EuBr$_2$- O')#,linestyle='dotted')#label='Eu$^{2+}$- Br$^-$',)
ax2.plot(cl_hdist,i_hist, '+', linewidth = '1', color='#ff5e00', linestyle='solid',label='EuI$_2$- O') #linestyle='--')     #label='Eu$^{2+}$- I$^-$',)

ax2.set_ylabel("CN", labelpad=12, fontsize=15, fontweight="bold")
ax2.set_ylim([-0.5,30])#4000])
#ax2.set_yticks(size=13)#, fontweight="bold")
#ax2.legend()
plt.legend(frameon=False, prop=font, loc='best')
plt.xticks(fontsize=13, fontweight="bold")
plt.yticks(fontsize=13, fontweight="bold")

plt.savefig("Eu-O_rdf_thf.png",
            dpi=200,
#            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True,
            facecolor ="w",
            edgecolor ='w',
            orientation ='landscape')
plt.show()
 
f.close()
g.close()
h.close()
i.close()
j.close()
k.close()
