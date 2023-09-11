#!/usr/bin/python
import numpy as np
import pandas as pd
import ReadLammpsTraj as RLT

class outputTraj(object):
	"""docstring for outputTraj"""
	def __init__(self, f):
		super(outputTraj, self).__init__()
		self.f = f

	def read_xyz(self,mframe,nframe,write_xyz):
		# 读取所有数据
		with open(self.f,"r") as f:
			atom_n = int(f.readline())
			print("Atom number =",atom_n)

		with open(self.f,"r") as f, open(write_xyz,"w") as traj:
			# print(f.readline())
			read_rows_0 = (atom_n+2)*(mframe)
			read_rows_1 = (atom_n+2)*(nframe+1)
			# print(read_rows_0,read_rows_1,read_rows_1-read_rows_0)
			for index, line in enumerate(f):
				# print(index,"-----",line)
				if index>=read_rows_0 and index<=read_rows_1:
					traj.write(line)
					print(read_rows_0,"-----",index,"-----",read_rows_1)
		return 

	def write_Ntraj(self,header,traj,write_traj):
		with open(write_traj,"w") as w:
			for h in range(len(header)):
				w.write(header[h])
			traj = traj.values
			m,n = traj.shape
			for i in range(m):
				for j in range(n):
					w.write(traj[i,j]+" ")
				w.write("\n")
		return 



import sys

if __name__ == '__main__':

	f = sys.argv[1]
	mframe = int(sys.argv[2])
	nframe = int(sys.argv[3])
	wfile = sys.argv[4]
	# path = "./"
	# f = path+"traj_npt_dissociation_330_11.lammpstrj"
	# mframe = 3001
	# nframe = mframe
	# wfile = ""
	if wfile == "":
		write_traj = "traj_"+str(mframe)+"-"+str(nframe)+".lammpstrj"
		write_xyz = "traj_"+str(mframe)+"-"+str(nframe)+".xyz"
	else:
		write_traj = wfile
		write_xyz = wfile

	opt = outputTraj(f)
	md = RLT.ReadLammpsTraj(f)
	md.read_info()
	if f.split(".")[-1]=="xyz":
		opt.read_xyz(mframe,nframe,write_xyz)
		print(write_xyz)
	elif f.split(".")[-1]=="lammpstrj":
		header = md.read_header(mframe)
		# print(header)
		traj = md.read_traj(mframe)
		opt.write_Ntraj(header,traj,write_traj)
		# print(traj)

	print(f)
	print("your ouput",mframe,"-",nframe,"th frame lammpstrj file")
	print("Job done!!!")