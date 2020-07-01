# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import sys
import h5py
sys.path.append("/Users/evancamp/astrochem/python/")
from tools import *

pwd = "/Users/evancamp/astrochem/learning/fig4_XRP/"

# Functions
def rho(tau,z):
    AU2cm = 14959790000000 # cm AU^-1
    r = 75*AU2cm # cm
    H = 3.5*AU2cm # cm
    z *= AU2cm # convert to cm
    k = float(sys.argv[1]) # cm^2 g^-1
    sig = tau/k
    mpdense = sig/(np.sqrt(2*np.pi)*H)
    zdep = np.exp(-z**2/(2*H**2))
    p = mpdense*zdep
    return p

# Setup input and model files
N = 29
sample_rate = (N-1)/14

height = np.linspace(0,14,N)
tau = np.logspace(1,-3,N)
A = 1.086*tau

rhos = []
for t,z in zip(tau,height):
    r = rho(t,z)
    rhos.append(r)
rhos = np.asarray(rhos)
n = rhos/1.67e-24

temp = []
T = 15
for z in height:
    if z < 6:
        temp.append(15)
    elif z <= 10:
        temp.append(T)
        T += 30/((10-6)*sample_rate)
    else:
        temp.append(45)
temp = np.asarray(temp)

suffix = "_k_{}".format(sys.argv[1])
inputFile = pwd+"input"+suffix+".ini"
sourceFile = pwd+"source"+suffix+".mdl"
chemFile = "/Users/evancamp/astrochem/networks/osu2009.chm"


with open(sourceFile,"w") as f:
    f.write("# cell number, Av [mag], n(H) [cm^-3], Tgas [K], Tdust [K], Height [AU]\n")
    linenumber = 0
    for i in range(N):
        f.write("{0}\t{1}\t{2}\t{3}\t{3}\t{4}\n".format(i,A[i],n[i],temp[i],height[i]))

chi = 1e3
abund = {
    "H2" : 0.5,
    "He" : 0.1,
    "H2O": 1e-4,
    "CO" : 5e-5
}
outputs = ["C2H","CO","CO2","H2O"]

###########################################
outstr = "abundances = "+",".join(outputs)+"\n"
with open(inputFile, "w") as f:
    # files
    f.write("[files]\n")
    f.write("source = {0}\nchem = {1}\n".format(sourceFile,chemFile))
    
    # physical param
    f.write("[phys]\n")
    f.write("chi = {}\n".format(chi))
    f.write("grain_gas_mass_ratio = 0.01\n")
    
    #solver param
    f.write("[solver]\n")
    f.write("ti = 1e-6\ntf = 1e6\n")
    
    #initial abundances
    f.write("[abundances]\n")
    for spec in abund.keys():
        f.write("{0}\t=\t{1}\n".format(spec,abund[spec]))
    
    #output
    f.write("[output]\n")
    f.write(outstr)
    #f.write("suffix = k_{}\n".format(sys.argv[1]))
    f.write("trace_routes = 1")
        