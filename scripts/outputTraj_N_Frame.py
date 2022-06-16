#!/usr/bin/python
import numpy as np
import pandas as pd
class outputTraj(object):
	"""docstring for outputTraj"""
	def __init__(self, f):
		super(outputTraj, self).__init__()
		self.f = f
	def read_info(self,):
		with open(self.f,'r') as f:
			L1 = f.readline()
			L2 = f.readline()
			L3 = f.readline()
			L4 = f.readline()
			L5 = f.readline()
			L6 = f.readline()
			L7 = f.readline()
			L8 = f.readline()
			L9 = f.readline().strip().split()[2:]#列标签
			self.col = L9
			step1 = int(L2)
			self.atom_n = int(L4)
			self.xlo,self.xhi = float(L6.split()[0]),float(L6.split()[1])
			self.ylo,self.yhi = float(L7.split()[0]),float(L7.split()[1])
			self.zlo,self.zhi = float(L8.split()[0]),float(L8.split()[1])
			self.Lx = self.xhi-self.xlo
			self.Ly = self.yhi-self.ylo
			self.Lz = self.zhi-self.zlo
			self.vlo = self.Lx*self.Ly*self.Lz
			for i in range(self.atom_n+1):
				Li = f.readline()
				# print(Li)
			step2 = int(f.readline())
			self.step_inter = step2-step1
			print("Step interval:",self.step_inter,"\nAtom number:",self.atom_n)
			print("xlo:",self.xlo,"xhi:",self.xhi,"Lx:",self.Lx)
			print("ylo:",self.ylo,"yhi:",self.yhi,"Ly:",self.Ly)
			print("zlo:",self.zlo,"zhi:",self.zhi,"Lz:",self.Lz)
		return self.step_inter,self.atom_n,self.Lx,self.Ly,self.Lz
		
	def read_traj(self,mframe,nframe,write_traj):
		# 读取所有数据
		# read_rows_0 = (self.atom_n+9)*(nframe-1)
		read_rows_0 = (self.atom_n+9)*(mframe)
		read_rows_1 = (self.atom_n+9)*(nframe+1)
		# print(read_rows_0,read_rows_1,read_rows_1-read_rows_0)
		with open(self.f,"r") as f, open(write_traj,"w") as traj:
			for index, line in enumerate(f,1):
				# print(index,"-----",read_rows_0,read_rows_1)
				if index>read_rows_0 and index<=read_rows_1:
					traj.write(line)
					print(read_rows_0,"-----",index,"-----",read_rows_1)
		return 


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

import sys

if __name__ == '__main__':
	#path = "./Interface/Steam3000_HeavyOil/473K/"
	#f = path+"traj_out_1.lammpstrj"
	#nframe = 1001
    f = sys.argv[1]
    mframe = int(sys.argv[2])
    nframe = int(sys.argv[3])
    wfile = sys.argv[4]
    if wfile == "":
        write_traj = "traj_"+str(mframe)+"-"+str(nframe)+".lammpstrj"
        write_xyz = "traj_"+str(mframe)+"-"+str(nframe)+".xyz"
    else:
        write_traj = wfile
        write_xyz = wfile

    opt = outputTraj(f)
    if f.split(".")[1]=="xyz":
    	opt.read_xyz(mframe,nframe,write_xyz)
    	print(write_xyz)
    else:
    	opt.read_info()
    	opt.read_traj(mframe,nframe,write_traj)
    	print(write_traj)

    print("you ouput",mframe,"-",nframe,"th frame lammpstrj file")
    print("Job done!!!")