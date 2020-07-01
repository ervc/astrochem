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

fig,axs = plt.subplots(2,2,figsize=(10,10))
axs = np.ndarray.flatten(axs)

for k in ks:
	kap = str(k)
	outfile = "astrochem_output_k_{}.h5".format(kap)
	specs = listspecies(outfile)
	for i in range(len(specs)):
		spec = specs[i]
		ax = axs[i]
		time,abun = readabun(outfile,spec)
		chemfile,srcfile = readfilesattrs(outfile)
		srcfile = srcfile.decode("utf-8")
		print(srcfile)

		height = []
		with open(srcfile,"r") as f:
			height = [float(line.split()[-1]) for line in f if line.split()[0] != "#"]

		height = np.asarray(height)
		final = abun[-1,:]
		ax.semilogx(final,height,label="$\kappa = {}$".format(kap))
		ax.set(xlabel = r"${0}$/H$_2$".format(totex(spec)))
for ax in axs:
	ax.set(
	    ylabel = "Z [AU]"
	)
	ax.legend()
# plt.savefig("all_kappa_all.png")
plt.show()