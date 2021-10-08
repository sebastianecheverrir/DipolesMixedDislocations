#!/home/sebastian/PythonEnvironments/EON35/bin/python

from ase.lattice.cubic 		import BodyCenteredCubic
from ase 			import Atom
from ase.io 			import write
from ase.io                     import read
from ase.calculators.lammpsrun 	import LAMMPS
from ase.optimize 		import BFGS
from ase.constraints 		import UnitCellFilter, ExpCellFilter

#Reading  a system that contains dislocated Fe 

FeLatticeConstant = 2.8553122

FeBulk_C = read('data.FeC_mixed_Relaxed', format='lammps-data', style='atomic')


#Removing some planes to add periodicity
#we detect the atom with the smallest x coordinate
min_x = min(FeBulk_C.positions[:,0])
#print(min_x)

#delete the atoms that hinder periodicity
del FeBulk_C[[atom.index for atom in FeBulk_C if atom.position[0]<min_x+2.3]] 

#Remove periodicity along y by increasing the size and centering the system
#FeBulk_C.cell[0][0] = FeBulk_C.cell[0][0]+20
#FeBulk_C.cell[1][1] = FeBulk_C.cell[1][1]+20

#restore periodicity along x
FeBulk_C.positions[:,0] = FeBulk_C.positions[:,0]-20/2
FeBulk_C.cell[0][0] = FeBulk_C.cell[0][0]-20-1.2

#b[:,:-1] = a



write('data.FeC_mixed_UnRelaxedPBCxz',  FeBulk_C, 'lammps-data')


