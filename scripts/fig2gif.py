#!/usr/bin/python
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import glob
from tqdm import tqdm

# 定义一个自定义的排序函数，从文件名中提取数字部分进行排序
def custom_sort(file_path):
    # 从文件路径中提取文件名
    file_name = os.path.basename(file_path)
    # 提取文件名中的数字部分作为排序关键字
    numeric_part = int(''.join(filter(str.isdigit, file_name)))
    time = file_name.split("_")[-1].split("ns")[0]
    # print(time)
    return numeric_part, time


def convert_pngs_to_gif(png_files, gif_file, duration=1.0):
    # try:
    # Create a list to store the frames
    frames = []

    # Read each PNG file and append it to the frames list
    for png_file in tqdm(png_files):
        time = png_file.split("_")[-1].split("ns")[0]
        img = Image.open(png_file)
        try:
            # 创建一个可以在图像上绘制文本的对象
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 150)
            draw.text((500, 50), time+" ns", fill="black", font=font)
        except:
            # print("Add text fail!")
            pass
        # 将 PIL 图像转换为 numpy 数组
        frame = np.array(img)
        frames.append(frame)

    # Save the frames as a GIF file
    imageio.mimsave(gif_file, frames, format='GIF', duration=duration)

    print(f"The FIG files have been converted to a GIF file '{gif_file}' successfully.")

    # except IOError:
    #     print("Unable to convert the PNG files to GIF.")

    return None


def print_usages():
    print("Usages:\n\t- fig2gif.py [figs_path] [gif_file] [duration]")
    print("\n\t- example: fig2gif.py ./2d/ output.gif 1")
    return None


import sys

print_usages()

if __name__ == "__main__":

    try:
        png_path = sys.argv[1]
    except:
        png_path = "./2d/"

    try:
        gif_file = sys.argv[2]
    except:
        gif_file = 'output.gif'

    try:
        png_files = glob.glob(os.path.join(png_path,'*.png'))
    except:
        png_files = glob.glob(os.path.join(png_path,'*.jpg'))

    # 对文件名进行排序
    sorted_png_files = sorted(png_files, key=custom_sort)

    # Convert the PNG files to GIF
    try:
        duration = float(sys.argv[3])
    except:
        duration = 5.0

    print("Your Command:\n\t- fig2gif.py",png_path,gif_file,duration)
    convert_pngs_to_gif(sorted_png_files, gif_file, duration=duration)
