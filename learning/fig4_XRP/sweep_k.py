from subprocess import check_call, DEVNULL
import numpy as np

ks = np.logspace(-3,3,7)

print(ks)

for k in ks:
	kap = str(k)
	check_call(["python","make_infiles.py",kap])
	print("made files with k = "+kap)
	check_call(["astrochem","input.ini"],stdout=DEVNULL)
	print("ran astrochem with k = "+kap)
	suffix = "_k_{}.h5".format(kap)
	check_call(["mv","astrochem_output.h5","astrochem_output"+suffix])
	print("changed outfile to astrochem_output"+suffix)
	check_call(["python","plotter.py",kap])
	print("plotted and saved k = "+kap)