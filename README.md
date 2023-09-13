## PyScripts
1. `lammpsdata2xyz.py`: it can convert the lammps data file to .xyz or .lammpstrj files
- command example:
```bash
lammpsdata2xyz.py xxx.data 
```
- Here, there should be a "# element" behind every mass in lammpsdata
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
5. `sort_trj.py`: it can sort lammpstrj file, according to the "id, mol, or type" 
- command example:
```bash
sort_trj.py  ./xxx.lammpstrj "id"
sort_trj.py  ./xxx.lammpstrj "mol"
sort_trj.py  ./xxx.lammpstrj "type"
```

6. `pdb2xyz.py`: it can convert the pdbfile to xyzfile 

```python
pdb2xyz.py ./xxx.pdb
pdb2xyz.py ./xxx.pdb xxx.xyz
```

7.  figures to gif file

```bash
fig2gif.py [figs_path] [gif_file] [duration]
fig2gif.py ./2d/ output.gif 1
```

8. convert lammpstrj file to a trjfile of meet [HTR](https://github.com/XueerPiaoaPiao/HTR)

```bash
to_HTR_lammpstrj.py -h
to_HTR_lammpstrj.py -i input.lammpstrj -o output_HTR.lammpstrj -fr 1 2
```

9. combine files to a file

```bash
combine_files.py ./temp/ traj_npt_dissociation_330_1.lammpstrj
```



## Dependencies

```
pip install -r requirements.txt
```



## make scripts to read

```bash
bash ./scripts/chmod.sh
```



