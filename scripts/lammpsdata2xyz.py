#!/usr/bin/python
# write xyz file from lammpsdata
import numpy as np
np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)

#read info from lammpsdata file
class LammpsData(object):
	def readAtominfo(self,lammpsdata):
		self.lammpsdata = lammpsdata
		with open(self.lammpsdata,'r') as data:
			for index, line in enumerate(data,1):
				if " atoms" in line:
					self.atom_number = int(line[:-6])
					print("Atom number =",self.atom_number)
				if "atom types" in line:
					self.atomtype_number = int(line[:-11])

				if "Atoms # full" in line:
					self.xyz_index_min = index
				elif "Velocities" in line:
					self.xyz_index_max = index
					# print(self.xyz_index_min,self.xyz_index_max)
				elif "Masses" in line:
					self.mass_index = index

		return print("xyz index in ["+str(self.xyz_index_min)+", "+str(self.xyz_index_max)+"]")

	def readXYZ(self,):
		xyz_array = np.loadtxt(self.lammpsdata,skiprows=self.xyz_index_min,max_rows=self.atom_number)
		# print(self.xyz)
		return xyz_array

	def AtomElement(self):
		with open(self.lammpsdata,"r") as data:
			for i in range(self.mass_index):
				data.readline()
			data.readline()
			atom_id = []
			element_id = []
			for j in range(self.atomtype_number):
				l = data.readline().strip().split()
				atom_type = l[0]
				element_type = l[3][0]
				atom_id.append(atom_type)
				element_id.append(element_type)
				# print(atom_type,element_type)
		atom_id = np.array(atom_id).reshape((-1,1))
		element_id = np.array(element_id).reshape((-1,1))
		id_element = np.hstack((atom_id,element_id))
		print(id_element.shape)
		return id_element

	def writeXYZfile(self,xyzdata,xyz_array):
		id_element = self.AtomElement()
		with open(xyzdata,'w') as xyzdata:
			xyzdata.write(str(self.atom_number)+'\n')
			xyzdata.write("Atoms. Timestep: 0\n")
			for i in range(self.atom_number):
				print(i,"-----------",self.atom_number)
				xyz_line=str(xyz_array[i,4:7]).strip('[').strip(']')
				for j in range(self.atomtype_number):
					if int(xyz_array[i,2]) == int(id_element[j,0]):
						xyzdata.write(id_element[j,1]+"\t"+xyz_line+'\n')


		return

# ---main program--- #
import sys

if __name__ == '__main__':
	print("\n------Start!------\n")
	# input data
	# lammpsdata = "system_oil_water.data"
	lammpsdata = sys.argv[1]
	# output xyz
	# xyzdata = 'system_oil_water.xyz'
	xyzdata = lammpsdata.split(".")[0]+'.xyz'
	# read atom info from data
	Ld = LammpsData()
	atom_number = Ld.readAtominfo(lammpsdata)
	xyz_array = Ld.readXYZ()
	Ld.writeXYZfile(xyzdata,xyz_array)

	print("\n------Done!------\n")