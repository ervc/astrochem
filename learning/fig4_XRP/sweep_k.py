from subprocess import check_call, DEVNULL
import numpy as np

mink = -3
maxk = 3
diff = maxk-mink+1
ks = np.logspace(mink,maxk,diff)

print(ks)

for k in ks:
	kap = str(k)
	suffix = "_k_{}".format(kap)

	check_call(["python","make_infiles.py",kap])
	print("made files with k = "+kap)

	check_call(["astrochem","input"+suffix+".ini"],stdout=DEVNULL)
	print("ran astrochem with k = "+kap)

	check_call(["mv","astrochem_output.h5","astrochem_output"+suffix+".h5"])
	print("changed outfile to astrochem_output"+suffix+".h5")

	check_call(["python","plotter.py",kap])
	print("plotted and saved k = "+kap)