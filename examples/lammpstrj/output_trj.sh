# compress the size of lammps dump file
for((i=0;i<=100;i++));do
echo $((j = $i * 100))
outputTraj_N_Frame.py traj_npt_relax_287_1.lammpstrj $j $j traj_npt_relax_287_1_${j}.lammpstrj
done

cat *0.lammpstrj > traj_npt_relax_287_1_save.lammpstrj

rm  *0.lammpstrj
