#!/usr/bin/python
import numpy as np
import pandas as pd
class SortTrj(object):
	"""docstring for outputTraj"""
	def __init__(self, f):
		super(SortTrj, self).__init__()
		self.f = f

	def sort(self,sortbyid="id"):
		trj = np.loadtxt(self.f,skiprows=9,dtype="str")
		if sortbyid == "id":
			trj_sort = trj[np.argsort(trj[:,0].astype(int))]
		elif sortbyid == "mol":
			trj_sort = trj[np.argsort(trj[:,2].astype(int))]
		elif sortbyid == "type":
			trj_sort = trj[np.argsort(trj[:,3].astype(int))]
		return trj_sort

	def write(self,sortbyid):
		trj_sort = self.sort(sortbyid)
		with open(self.f,"r") as f, open("sort_"+self.f,"w") as w:
			for i in range(9):
				w.write(f.readline())
			m,n = trj_sort.shape
			# print(m,n)
			trj_sort[:,0] = np.linspace(1,m,m).astype(int)
			print(trj_sort[:,0])
			for j in range(m):
				for k in range(n):
					w.write(trj_sort[j,k]+"\t")
				w.write("\n")
		return

import sys

if __name__ == '__main__':
	# f = "out_1000.lammpstrj"

	f = sys.argv[1]
	sortbyid = sys.argv[2]
	st = SortTrj(f)
	st.write(sortbyid)
	print("Job done!!!")