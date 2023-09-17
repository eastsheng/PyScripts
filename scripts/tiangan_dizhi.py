#!/usr/bin/python
# 给出年份，计算中国古代天干地支纪年
import argparse

tiangan    = {4:"甲",5:"乙",6:"丙",7:"丁",8:"戊",9:"己",0:"庚",1:"辛",2:"壬",3:"癸"}
dizhi      = {4:"子",5:"丑",6:"寅",7:"卯",8:"辰",9:"巳",10:"午",11:"未",0:"申",1:"酉",2:"戌",3:"亥"}
shengxiao  = {4:"鼠🐀",5:"牛🐂",6:"虎🐅",7:"兔🐇",8:"龙🐉",9:"蛇🐍",10:"马🐎",11:"羊🐏",0:"猴🐒",1:"鸡🐓",2:"狗🐕",3:"猪🐖"}

def find_td_year(year):
	t = int(year%10)
	d = int(year%12)
	year_td = tiangan[t]+dizhi[d]
	sx = shengxiao[d]
	print(20*"-")
	print("\n%d年: %s %s年\n" % (year, year_td, sx))
	print(20*"-")
	return


def find_gy_year(year_td):
	t = year_td[0][0]
	d = year_td[0][1]

	try:
		y = int(year_td[1])
	except:
		y = 2000
	tiangan_new = dict(zip(tiangan.values(), tiangan.keys()))
	dizhi_new   = dict(zip(dizhi.values(), dizhi.keys()))
	tt = tiangan_new[t]
	dd = dizhi_new[d]
	print(20*"-")
	print("%s%s年可能是：" %(t,d))

	for i in range(y-30,y+31):
		if i%10==tt and i%12 == dd:
			print("\t%s %s年" % (i, shengxiao[dd]))
	print(20*"-")
	return


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='给出年份，计算中国古代天干地支纪年')
	parser.add_argument('-t','--tdyear', type=int, help='给出公元纪年，计算天干地支纪年，如：python tiangan_dizhi.py -t 2000')
	parser.add_argument('-g','--gyyear', type=str, nargs='+', 
		help='给出天干地支纪年以及大概的公元年，计算准确公元纪年，如：python tiangan_dizhi.py -g 甲申 2000')

	args = parser.parse_args()
	if args.tdyear:

		try:
			find_td_year(args.tdyear)
		except:
			print(20*"-")
			print("Error: -t args Input error")
			print(20*"-")

	if args.gyyear:

		try:
			find_gy_year(args.gyyear)
		except:
			print(20*"-")
			print("Error: -g args Input error")
			print(20*"-")
