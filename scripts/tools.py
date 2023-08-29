#!/usr/bin/python
import sys
import os

examples = {
    "tools":["tools "],
    "lammpsdata2xyz":["lammpsdata2xyz.py xxx.data"],
    "pdb2xyz":["pdb2xyz.py xxx.pdb"],
    "msi2clayff":["msi2clayff.py xxx.data"],
    "png2tif":["png2tif.py png_name tif_name fig_quality"],
    "outputTraj_N_Frame":["outputTraj_N_Frame.py  xxx.lammpstrj 0 10 output.lammpstrj",
                        "outputTraj_N_Frame.py  xxx.xyz 0 10 output.xyz"],
    # "msd_diffusion":["msd_diffusion.py --help"],
    "sort_trj":["sort_trj.py xxx.lammpstrj 'mol' "],
    "fig2gif":["fig2gif.py ./2d/ output.gif 1"],
    "to_HTR_lammpstrj":["to_HTR_lammpstrj.py -i input.lammpstrj -o output_HTR.lammpstrj -fr 1 2"],
}


def getFileStr(level):
    return '   '*level+'- '
def getDicStr(level):
    return '\t'*level+'+'

def printFile(path,level):
    if os.path.exists(path):   
        files = os.listdir(path)
        for f in files :
            subpath=os.path.join(path,f)
            print("  ",50*"..")
            if os.path.isfile(subpath):
                if f.endswith('.py')==True:
                    name = f.split(".")[0]
                    # print(50*"..")
                    print(getFileStr(level)+os.path.basename(subpath))
                    for i in range(len(examples[name])):
                        print(getFileStr(level+1)+"e.g."+"# "+examples[name][i])
            else:
                leveli=level+1
                print(getDicStr(level)+os.path.basename(subpath))
if __name__ == "__main__":
    # printFile("/home/chends/softwares/my_python_packages/",1)
    path = sys.path[0]
    print("- "*22,"PyScripts"," -"*22)
    print("Project: https://github.com/eastsheng/PyScripts")
    print("+  tools")
    printFile(path,1)
    print("- "*22,"PyScripts"," -"*22)