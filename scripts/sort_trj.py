#!/usr/bin/python
import numpy as np
import pandas as pd
class SortTrj(object):
	"""docstring for outputTraj"""
	def __init__(self, f):
		super(SortTrj, self).__init__()
		self.f = f

	def sort(self,):
		trj = np.loadtxt(self.f,skiprows=9,dtype="str")
		trj_sort = trj[np.argsort(trj[:,0].astype(int))]
		return trj_sort

	def write(self,):
		trj_sort = self.sort()
		with open(self.f,"r") as f, open("sort_"+self.f,"w") as w:
			for i in range(9):
				w.write(f.readline())
			m,n = trj_sort.shape
			# print(m,n)
			for j in range(m):
				for k in range(n):
					w.write(trj_sort[j,k]+"\t")
				w.write("\n")
		return

import sys

if __name__ == '__main__':
	# f = "out_1000.lammpstrj"
	f = sys.argv[1]
	st = SortTrj(f)
	st.write()
	print("Job done!!!")