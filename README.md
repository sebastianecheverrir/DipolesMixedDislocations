# Dipoles Mixed Dislocations

Scripts to generate systems containing dipoles of dislocations to be used to run molecular dynamics simulations with [Lammps](https://lammps.sandia.gov/). All the dislocations are of the type  1/2<111> and the glide plane is {110} in b.c.c. crystals (Fe).

The character of the dislocations is given by their angle, as shown in the following table. The x, y and z values represent the orientation of the crystal in the simulation box. For each dislocation character, a folder is included. To generate the system, execute the bash file  `main_Fe_mixed.sh`. It produces a file called `data.FeC_mixed_Relaxed` containing the dislocation dipole (and an interstitial C atom.)

The boxes are oriented in such a way that the dislocation line is parallel to the z direction,and the glide plane is y. b_x and b_z correspond to the edge and screw components of the burgers vector of the dislocations. 

|Angle|x|y|z|b_x|b_z|
|-|-|-|-|-|-|
|0.000000 |[1, 2, 1]  |[-1, 0, 1]|[1, -1, 1]  |0.000000|2.472773|
|10.024988|[1, 3, 1]  |[-1, 0, 1]|[3, -2, 3]  |0.430455|2.435018|
|19.471221|[1, 1, 1]  |[-1, 0, 1]|[1, -2, 1]  |0.824258|2.331353|
|29.496208|[3, 2, 3]  |[-1, 0, 1]|[1, -3, 1]  |1.217509|2.152273|
|35.264390|[0, 1, 0]  |[-1, 0, 1]|[1, 0, 1]   |1.427656|2.019011|
|54.735610|[1, 0, 1]  |[-1, 0, 1]|[0, -1, 0]  |2.019011|1.427656|
|60.503792|[-1, 3, -1]|[-1, 0, 1]|[3, 2, 3]   |2.152273|1.217509|
|70.528779|[-1, 2, -1]|[-1, 0, 1]|[1, 1, 1]   |2.331353|0.824258|
|79.975012|[3, -2, 3] |[-1, 0, 1]|[-1, -3, -1]|2.435018|0.430455|
|90.000000|[1, -1, 1] |[-1, 0, 1]|[-1, -2, -1]|2.472773|0.000000|

Included is also the script `ListMixedDislocations.py`, which can be used to calculate all the 1/2<111> dislocations on  {110}  planes in b.c.c. crystals. 

#### Software Dependencies
- [Lammps](https://lammps.sandia.gov/)    
- [Atomsk](https://atomsk.univ-lille.fr/)   
- [Python 3](https://www.python.org/)
- [ASE](https://wiki.fysik.dtu.dk/ase/)      


