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
			# print("Atom number =",atom_n)

		with open(self.f,"r") as f, open(write_xyz,"w") as traj:
			# print(f.readline())
			read_rows_0 = (atom_n+2)*(mframe)
			read_rows_1 = (atom_n+2)*(nframe+1)
			# print(read_rows_0,read_rows_1,read_rows_1-read_rows_0)
			for index, line in enumerate(f):
				# print(index,"-----",line)
				if index>=read_rows_0 and index<=read_rows_1:
					traj.write(line)
					# print(read_rows_0,"-----",index,"-----",read_rows_1)
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

	try:
		f = sys.argv[1]
	except:
		f = "traj_npt_dissociation_330_11.lammpstrj"
	try:	
		mframe = int(sys.argv[2])
		nframe = int(sys.argv[3])
	except:
		n = 0
		mframe = n
		nframe = n
	try:
		wfile = sys.argv[4]
	except:
		wfile = "traj_npt_dissociation_330_"+str(mframe)+"_"+str(nframe)+".lammpstrj"	

	opt = outputTraj(f)
	md = RLT.ReadLammpsTraj(f)
	# md.__version__()
	md.read_info()
	if f.split(".")[-1]=="xyz":
		wfile = wfile.split(".lam")[0]+".xyz"
		opt.read_xyz(mframe,nframe,wfile)
		# print(write_xyz)
	elif f.split(".")[-1]=="lammpstrj":
		header = md.read_header(mframe)
		# print(header)
		traj = md.read_traj(mframe)
		opt.write_Ntraj(header,traj,wfile)
		# print(traj)

	# print(f)
	# print("your ouput",mframe,"-",nframe,"th frame lammpstrj file")
	# print("Job done!!!")
