import numpy as np
import matplotlib.pyplot as plt
import sys
import h5py
sys.path.append("/Users/evancamp/astrochem/python/")
from tools import *
from tools import _totex_species as totex

kap = "unknown"
if len(sys.argv) > 1:
	kap = str(sys.argv[1])

pwd = "/Users/evancamp/astrochem/learning/fig4_XRP/"

# read outfile and get times, abundances, and input files
spec = "C2H"
outfile = pwd+"/astrochem_output_k_{}.h5".format(kap)
time,abun = readabun(outfile,spec)
chemfile,srcfile = readfilesattrs(outfile)
srcfile = srcfile.decode("utf-8")

height = []
with open(srcfile,"r") as f:
	height = [float(line.split()[-1]) for line in f if line.split()[0] != "#"]

height = np.asarray(height)

final = abun[-1,:]

fig,ax = plt.subplots()

ax.semilogx(final,height)
ax.set(
    xlim = (1e-15,1e-7),
    xlabel = r"${0}$/H$_2$".format(totex(spec)),
    ylabel = "Z [AU]"
)
plt.title("$\kappa = {}$".format(kap))
plt.savefig("C2H_k_{}.png".format(kap))
# plt.show()