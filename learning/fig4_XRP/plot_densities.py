import matplotlib.pyplot as plt
import numpy as np
# import h5py
import sys
sys.path.append("/Users/evancamp/astrochem/python/")
from tools import *
from tools import _totex_species as totex

mink = -3
maxk = 3
diff = maxk-mink+1
ks = np.logspace(mink,maxk,diff)

fig,ax = plt.subplots()

for k in ks:
	kap = str(k)
	outfile = "astrochem_output_k_{}.h5".format(kap)
	specs = listspecies(outfile)

	chemfile,srcfile = readfilesattrs(outfile)
	srcfile = srcfile.decode("utf-8")
	print(srcfile)

	with open(srcfile,"r") as f:
		height = [float(line.split()[-1]) for line in f if line.split()[0] != "#"]
	with open(srcfile,"r") as f:
		dens = [float(line.split()[2]) for line in f if line.split()[0] != "#"]
	height = np.asarray(height)
	dens = np.asarray(dens)

	ax.semilogx(dens,height,label="$\kappa = {}$".format(kap))
ax.set(
	xlabel = "nh",
    ylabel = "Z [AU]"
)
ax.legend()
# plt.savefig("all_kappa_all.png")
plt.show()