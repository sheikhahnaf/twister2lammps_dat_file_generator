# twister2lammps_dat_file_generator
#! A python script to convert output of twister code into a dat file in lammps format.


!!TWISTER is a python package that helps you construct 
commensurate superlattices on introducing a twist between 
2D materials. If you use this package please cite the following 
paper for which this code was developed:
"Ultraflatbands and Shear Solitons in Moire Patterns of Twisted Bilayer
Transition Metal Dichalcogenides", Phys. Rev. Lett. 121, 266401 (2018) 
(https://doi.org/10.1103/PhysRevLett.121.266401)

!!LAMMPS is a software package for molecular dynamics simulation.

This python script facilitates converting output from TWISTER which generally provides co-ordinates for a definite twist angle of 2D bilayer structures to a file 
readable by lammps for taking in the co-ordinates of atoms.


NOTE: The twister generated file have to be manually stripped of lines other than the atom co-ordinates. 
