# The theoretical Maxwell-Boltzmann velocity distribution
# f(vi) = [(m/(2*pi*kB*T))^(0.5)]*exp((-m*vi^2)/(2*kB*T))

import numpy as np
import matplotlib.pyplot as plt
import fastdataing as fd

def vel_distribution(paramters):
	kB = 1.380649e-23 # J/K
	amu2kg = 6.02214076208112e26
	temperature = paramters["temperature"]
	mass = paramters["mass"]/amu2kg
	x_range = paramters["x_range"]
	v = np.linspace(x_range[0],x_range[1],x_range[2])
	a0 = 2.0*np.pi*kB*temperature
	a1 = 2.0*kB*temperature
	b = np.sqrt(mass/a0)
	c = -mass*(v*v)/a1
	f = b*np.exp(c)
	print(b)
	return v, f

def plot(x,y):
	fig = fd.add_fig()
	plt.subplots_adjust(left=0.15,bottom=0.15)
	ax = fd.add_ax(fig)
	fd.plot_fig(ax,x[::5],y[::5],color="ro-",linewidth=1.5,label="Ar-300 K",
		xlabel=r"$\regular \it v_i$ (m/s)",
		ylabel=r"$\regular \it f(v_i)$")
	ax.set_xlim(-1000,1000)
	ax.set_yticks([0,0.0005,0.001,0.0015])
	# ax.set_ylim(0,)
	ax.set_title("Maxwell-Boltzmann velocity distribution")
	plt.savefig("MaxwellBoltzmann_vel_distribution.png",dpi=300)
	plt.show()
	return

if __name__ == '__main__':
	paramters = {
	"temperature": 300, # K
	"mass": 39.948, # Ar
	"x_range":(-2000,2000,1000)
	}
	v,f = vel_distribution(paramters)
	plot(v,f)