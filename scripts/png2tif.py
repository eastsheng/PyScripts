#!/usr/bin/python
from PIL import Image
import sys

def png2tif(fig,fig_new,quality=100):
	"""
	png2tif.py fig_name tif_name fig_quality
	"""
	img = Image.open(fig,"r")
	img.save(fig_new,quality=quality)


if __name__ == '__main__':
	try:
		argv = sys.argv[1:]
		if len(argv)==1:
			fig = argv[0] # 传入参数1：图片名称
			fig_new = "{}.tif".format(fig.split(".")[0]) # 传入参数2：图片默认精度100
			quality = 100 # 传入参数2：图片默认精度100
		elif len(argv)==2:
			fig = argv[0] # 传入参数1：图片名称
			fig_new = argv[1] # 传入参数2：tiff图片名称
			quality = 100 # 传入参数2：图片默认精度100		
		elif len(argv)==3:
			fig = argv[0] # 传入参数1：图片名称
			fig_new = argv[1] # 传入参数2：tiff图片名称
			quality = argv[2] # 传入参数2：图片精度			
		print("图片文件名为：",fig)
		print("tiff图片文件名为：",fig_new)
		print("图片质量为：",quality)
	except:
		print("未输入文件名参数，或输入错误...")
		pass

	png2tif(fig,fig_new,quality)
