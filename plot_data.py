import sys
import matplotlib.pyplot as plt
import numpy as np
import h5py

args = sys.argv
if len(args) < 2 or len(args) > 3:
	print("Please provide astrochem output file:\npython plot_data.py infile [outfile]")
	quit()
filename = args[1]

if len(args) == 3:
	outfile = args[2]
else:
	outfile = "abun_plt.png"

print("infile = ",filename)
print("outfile = ",outfile)

with h5py.File(filename, "r") as f:
    # List all groups
    keys = list(f.keys())

    # Get the data
    abun = np.asarray(f[keys[0]])[0]
    rout = np.asarray(f[keys[1]])
    spec = np.asarray(f[keys[2]])
    time = np.asarray(f[keys[3]])
    
    
    fig,ax = plt.subplots(figsize=(5,5))
    plt.title("Abundances")
    X = time
    for i in range(len(abun[0])):
        Y = [abun[j][i] for j in range(len(abun))]
        label = spec[i].decode('utf-8')
        if (i!=2):
            ax.loglog(X,Y,label=label)
    
    plt.legend()
    ax.set(
        xlim=(1e0,1e7),
        ylim=(1e-12,1e-4),
        xlabel="Time (yr)",
        ylabel="$n(x)/n_H$")
    plt.savefig(outfile)