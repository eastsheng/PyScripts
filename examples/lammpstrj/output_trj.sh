# compress the size of lammps dump file
for((i=0;i<=100;i++));do
echo $((j = $i * 100))
outputTraj_N_Frame.py traj_npt_relax_287_1.lammpstrj $j $j ./temp/traj_npt_relax_287_1_${j}.lammpstrj
done

combine_files.py ./temp/ traj_npt_relax_287_1_save.lammpstrj

rm -rf ./temp/
