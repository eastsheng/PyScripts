## ./scripts/
1. `lammpsdata2xyz.py`: it can convert the lammps data file to .xyz or .lammpstrj files
- command example:
```bash
lammpsdata2xyz.py xxx.data 
```
2. `msi2clayff.py`: it can convert the obtained hydroxylated SiO2 lammps data from `msi2lmp.exe` tool to lammps data with clayff force fields 
- command example:
```bash
msi2clayff.py xxx.data
```
3. `png2tif.py`: it can convert the png to tif
- command example:
```bash
png2tif.py png_name tif_name fig_quality
```
4. `outputTraj_N_Frame.py`: it can out put the lammpstrj file, any frame
- command example:
```bash
outputTraj_N_Frame.py  ./xxx.lammpstrj 0 10 ./output.lammpstrj
outputTraj_N_Frame.py  ./xxx.xyz 0 10 ./output.xyz
```

## make pyscripts to read
```bash
bash chmod.sh
```
