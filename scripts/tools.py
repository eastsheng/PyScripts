#!/usr/bin/python
import sys
import os

examples = {
    "tools":["tools "],
    "lammpsdata2xyz":["lammpsdata2xyz.py xxx.data"],
    "msi2clayff":["msi2clayff.py xxx.data"],
    "png2tif":["png2tif.py png_name tif_name fig_quality"],
    "outputTraj_N_Frame":["outputTraj_N_Frame.py  xxx.lammpstrj 0 10 output.lammpstrj",
                        "outputTraj_N_Frame.py  xxx.xyz 0 10 output.xyz"],
    "msd_diffusion":["msd_diffusion.py --help"],

}


def getFileStr(level):
    return '  '*level+'- '
def getDicStr(level):
    return '  '*level+'+'

def printFile(path,level):
    if os.path.exists(path):   
        files = os.listdir(path)
        for f in files :
            subpath=os.path.join(path,f)
            if os.path.isfile(subpath):
                if f.endswith('.py')==True:
                    name = f.split(".")[0]
                    print(50*"-")
                    print(getFileStr(level)+os.path.basename(subpath))
                    for i in range(len(examples[name])):
                        print(getFileStr(level+1)+"e.g."+"# "+examples[name][i])
            else:
                leveli=level+1
                print(getDicStr(level)+os.path.basename(subpath))

# printFile("/home/chends/softwares/my_python_packages/",1)

print("+  tools")
printFile("/home/cup/softwares/PyScripts/scripts",1)