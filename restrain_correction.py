import numpy as np
import math

def RestrainCorrection(flatbottomtrestrain,outterforceconst, innerradius):
    fo=outterforceconst
    pi=np.pi
    gasconst=8.314/4184
    temp=298.15
    kt = temp * gasconst
    stdcon = (1.0*10**27) / (6.02214 * 10**23)

    if flatbottomtrestrain==True:
        ri=0
        fi=1
    else:
        ri=innerradius
        fi=outterforceconst
#    ri=restraintdistance
#    fi=distancerestraintconstant
#    ri=0
#    fi=1

    ro=innerradius
    v1 = 2.0*pi*ri*(-2.0+np.exp(-ri**2*fi/kt))*kt/fi + np.sqrt(kt*(pi/fi)**3)*(2.0*fi*ri*ri+kt)*math.erf(ri*np.sqrt(fi/kt))
    v2 = (4.0*pi/3.0) * (ro**3-ri**3)
    v3 = np.sqrt(kt*(pi/fo)**3) * (2.0*fo*ro*ro+kt+4.0*ro*np.sqrt(kt*fo/pi))
    vol = v1 + v2 + v3
    dv1 = 2.0*pi*ri**3*np.exp(-ri**2*fi/kt)/temp + 2.0*pi*ri*(-2.0+np.exp(-ri**2*fi/kt))*kt/(fi*temp) + 0.5*np.sqrt((pi/fi)**3)*np.sqrt(kt)*(2.0*ri**2*fi+kt)*math.erf(ri*np.sqrt(fi/kt))/temp - pi*ri*np.exp(-ri**2*fi/kt)*(2.0*ri**2*fi+kt)/(fi*temp) + np.sqrt((kt*pi/fi)**3)*math.erf(ri*np.sqrt(fi/kt))/temp
    dv2 = 0.0
    dv3 = np.sqrt(kt*(pi/fo)**3)*fo*ro*ro/temp + 4.0*kt*(pi/fo)*ro/temp + 1.5*np.sqrt((kt*pi/fo)**3)/temp
    dvol = dv1 + dv2 + dv3
    dg = -kt * np.log(vol/stdcon)
    ds = -dg/temp + kt*dvol/vol
    dh = dg + temp*ds
    return dg,dh,ds
    
a = RestrainCorrection(True,5.0,2.6)
b = RestrainCorrection(False,5.0,2.6)


print(" flat-bottomed dG correction: ",round(a[0],3)," Kcal/mol")
print(" flat-bottomed dH correction: ",round(a[1],3)," Kcal/mol")
print(" flat-bottomed dS correction: ",round(a[2],3)," Kcal/mol")
print('')
print("               dG correction: ",round(b[0],3)," Kcal/mol")
print("               dH correction: ",round(b[1],3)," Kcal/mol")
print("               dS correction: ",round(b[2],3)," Kcal/mol")

