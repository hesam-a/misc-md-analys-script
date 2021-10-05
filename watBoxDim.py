# A program for measuring a periodic box dimensions by Hesam A @FSU

from itertools import islice
import sys

def xyzReader(a):
    b=[]
    x_coord=[]
    y_coord=[]
    z_coord=[]
    highest = 0
    for line in islice(a, 2, None):
        b=line.split()
        x_coord.append(float(b[1]))
        y_coord.append(float(b[2]))
        z_coord.append(float(b[3]))
    x_coord.sort()
    y_coord.sort()
    z_coord.sort()
    print('')
    print(x_coord,"max= ",x_coord[-1], "min =", x_coord[0])
    print(y_coord,"max= ",y_coord[-1], "min =", y_coord[0])
    print(z_coord,"max= ",z_coord[-1], "min =", z_coord[0])
    print ('')
    max_x = abs(x_coord[-1])+abs(x_coord[0])
    max_y = abs(y_coord[-1])+abs(y_coord[0])
    max_z = abs(z_coord[-1])+abs(z_coord[0]) 
    if max_x > highest:
        highest = max_x
    if max_y > highest:
        highest = max_y 
    elif max_z > highest:
        highest = max_z

    print(' Dimensions are based on vdW cutoff of 12 Angstrom')
    print('')
    print( 'max_x = ', max_x+24)
    print( 'max_y = ', max_y+24)
    print( 'max_z = ', max_z+24)
    print('')
    print ( 'Highest size: ', round(highest,6)+ 24.0, 'pick this one!')
    return round(highest,6)+ 24.0

def molecPerAngs(density, molecweight):
    return (density * 0.6022) / molecweight 


def main():
    """ The first argument is the molecule coordinates file name/
        The second argument is the density of the molecule/
        The third argument is the molecular weight of the molecule/
        If the fourth argument is entered (randomly), the program will run the first if statement/
        If only the first THREE arugemnts are used, the program will run the elif statement /
        If only the first TWO arugemnts are used, the program will run the elif statement/


        """
    if len(sys.argv) == 5: 
        f = open(sys.argv[1],'r')
        density = float(sys.argv[2])
        molecweight = float (sys.argv[3])
        a = xyzReader(f)
        print('')
        print(' Density of your atom/molecule (should be in g/cm3, IF NOT, convert it!): ',density)
        print('')
        print(' Molecular weight of your atom/molecule: ', molecweight, 'g/mol')
        print('')
        molecpermolec = molecPerAngs(density,molecweight) 
        print(round(molecpermolec, 4), 'Molecules per Angstrom')
        print('')
        print(' You need', round(molecpermolec * a**3,0), 'molecules for your box!')
        print('')
    elif len(sys.argv) == 4:
        density = float(sys.argv[1])
        molecweight = float (sys.argv[2])
        side_size = float (sys.argv[3])
        print('')
        print(' Density of your atom/molecule: ',density)
        print(' Molecular weight of your atom/molecule: ', molecweight, 'g/mol')
        print('')
        molecpermolec = molecPerAngs(density,molecweight) 
        print(round(molecpermolec,4), 'Molecules per Angstrom')
        print('')
        print(' You need', round(molecpermolec * side_size**3,0), 'molecules for your box!')
        print('')
    elif len(sys.argv) == 3:
        density = float(sys.argv[1])
        molecweight = float (sys.argv[2])
        print('')
        print(' Density of your atom/molecule: ',density)
        print(' Molecular weight of your atom/molecule: ', molecweight, 'g/mol')
        print('')
        molecpermolec = molecPerAngs(density,molecweight) 
        print(round(molecpermolec,4), 'Molecules per Angstrom')
        print('')
    elif len(sys.argv) == 2:
        f = open(sys.argv[1],'r')
        xyzReader(f)
        print('')



if __name__ == "__main__":
    main()
