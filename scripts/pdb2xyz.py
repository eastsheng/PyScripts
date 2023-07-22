#!/usr/bin/python
# write xyz file from pdb file
import sys

def pdb2xyz(pdbfile,xyzfile):
	new_line = []
	with open(pdbfile,"r") as f, open(xyzfile,"w") as w:
		for index, line in enumerate(f):
			if "ATOM" in line:
				element = line[76:78]
				x = line[31:38]
				y = line[39:46]
				z = line[47:54]
				print(element,x,y,z)
				new_line.append([element,x,y,z])

		atom_number = len(new_line)
		w.write(str(atom_number)+"\n")
		w.write("generted by 'pdb2xyz.py'\n")
		for i in range(atom_number):
			w.write(new_line[i][0]+"\t"+new_line[i][1]+"\t"+\
				    new_line[i][2]+"\t"+new_line[i][3]+"\n")
	return


if __name__ == '__main__':
	print("\n------Start!------\n")
	# pdbfile = "quartz_pore.pdb"
	pdbfile = sys.argv[1]
	try:	
		xyzfile = sys.argv[2]
	except:
		xyzfile = pdbfile.split(".")[0]+'.xyz'
	pdb2xyz(pdbfile,xyzfile)
	print("\n------Done!------\n")	