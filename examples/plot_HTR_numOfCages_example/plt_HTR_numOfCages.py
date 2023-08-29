import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_numOfCages(numOfCages_file):
	df = pd.read_csv(numOfCages_file,delimiter = "\t",index_col=0)

	df.index = list(map(lambda i: int(i.split(":")[0].strip()), df.index))
	df.columns = list(map(lambda j: j.split(":")[0].strip(), df.columns))

	new_columns = df.columns[1:]
	new_df = df.iloc[:,:-1]

	new_df.columns = new_columns

	return new_df


if __name__ == '__main__':

	timestep = 2 # fs
	interste = 10000
	fs2ns = 1e-6
	numOfCages_file = "./output.cages"

	plt.rc('font', family='Times New Roman', size=18)
	fig = plt.figure(figsize=(12,8))
	# fig.subplots_adjust(bottom=0.2,left=0.2,hspace=0.3)	
	ax=fig.add_subplot(111)
	new_df = read_numOfCages(numOfCages_file)
	time = new_df.index.values*interste*timestep*fs2ns
	print(new_df)
	print(new_df.columns)	

	num_of_512cages = new_df["0-12-0"]
	num_of_51262cages = new_df["0-12-2"]

	ax.plot(time,num_of_512cages,"r",label=r"$\regular5^{12}$",linewidth=2)
	ax.plot(time,num_of_51262cages,"g",label=r"$\regular5^{12}6^2$",linewidth=2)
	
	ax.legend(loc="best")
	ax.set_xlabel('Time (ns)',fontweight='bold',size=22)
	ax.set_ylabel('Number of cages',fontweight='bold',size=22)
	ax.set_xlim(0,60)
	ax.set_ylim(0,)
	plt.show()	