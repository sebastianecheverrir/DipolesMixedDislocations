#!/home/sebastian/PythonEnvironments/EON35/bin/python

from ase.lattice.cubic 		import BodyCenteredCubic
from ase 			import Atom
from ase.io 			import write
from ase.io                     import read
from ase.calculators.lammpsrun 	import LAMMPS
from ase.optimize 		import BFGS
from ase.constraints 		import UnitCellFilter, ExpCellFilter
from random import uniform


#Reading  a system that contains dislocated Fe 

#FeLatticeConstant = 2.8553122

FeBulk = read('Fe_mixed.lmp', format='lammps-data', style='atomic')

#adding a C atom

xPosition = uniform(0,FeBulk.cell[0][0])
yPosition = uniform(0,FeBulk.cell[1][1])
zPosition = uniform(0,FeBulk.cell[2][2])

Csingle =  Atom('C', position=(xPosition, yPosition, zPosition))


FeBulk_C = FeBulk + Csingle


#Remove periodicity along x by increasing the size and centering the system
FeBulk_C.cell[0][0] = FeBulk_C.cell[0][0]+20
#FeBulk_C.cell[1][1] = FeBulk_C.cell[1][1]+20
FeBulk_C.positions[:,0] = FeBulk_C.positions[:,0]+20/2

#b[:,:-1] = a



write('data.FeC_mixed_UnRelaxed',  FeBulk_C, 'lammps-data')


