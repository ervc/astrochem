import matplotlib.pyplot as plt
import numpy as np
# import h5py
import sys
sys.path.append("/Users/evancamp/astrochem/python/")
from tools import *
from tools import _totex_species as totex

ks = np.logspace(-3,3,7)
spec = "CO2"

fig,ax = plt.subplots()

for k in ks:
	kap = str(k)
	outfile = "astrochem_output_k_{}.h5".format(kap)
	time,abun = readabun(outfile,spec)
	chemfile,srcfile = readfilesattrs(outfile)
	srcfile = srcfile.decode("utf-8")

	height = []
	with open(srcfile,"r") as f:
		height = [float(line.split()[-1]) for line in f if line.split()[0] != "#"]

	height = np.asarray(height)
	final = abun[-1,:]
	ax.semilogx(final,height,label="$\kappa = {}$".format(kap))
ax.set(
    xlabel = r"${0}$/H$_2$".format(totex(spec)),
    ylabel = "Z [AU]"
)
ax.legend()
plt.savefig("all_kappa_{}.png".format(spec))
# plt.show()