#!/usr/bin/python
"""
# convert lammpstrj file to a trjfile of meet HTR: id type x y z
# only save type 1 (O atom) information
# pip install ReadLammpsTraj
"""
import ReadLammpsTraj as RLT
from tqdm import tqdm
import sys
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', type=str, help='input lammpstrj file, example: -i input.lammpstrj')
	parser.add_argument('-o', type=str, help='output lammpstrj file, example: -o output.lammpstrj')
	parser.add_argument('-fr', type=int, default=[1,1 1], nargs='+', help='range of frames, example: -fr 1 100 1')
	args = parser.parse_args()
	inputfile = args.i

	try:
		outputfile = args.o
	except:
		outputfile = inputfile.split(".")[0]+"HTR.lammpstrj"
	
	mframe,nframe, interval = args.fr[0], args.fr[1], args.fr[2]
	
	md = RLT.ReadLammpsTraj(inputfile)
	md.read_info()
	w =open(outputfile,"w")
	for i in tqdm(range(mframe,nframe+1,interval)):
		traj = md.read_traj(i)[["id","type","x","y","z"]]
		new_traj = traj[traj['type']=="1"].values
		m, n = new_traj.shape
		header = md.read_header(i)
		for h in range(len(header)):
			if h == 3:
				w.write(str(m)+"\n")
			elif h == len(header)-1:
				w.write("ITEM: ATOMS id type x y z\n")
			else:
				w.write(header[h])

		for mi in range(m):
			for ni in range(n):

				w.write(new_traj[mi,ni]+" ")
			w.write("\n")
	w.close()
	print("convert lammpstrj to meet the HTR successfuly!")
	