import numpy as np
import collections
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font',family = 'serif', size=15)

def closedBoxFrac(Z,z0,y):
    if not isinstance(Z, collections.Iterable):
        Z = [Z]
    s_per_M0 = []
    for z in Z:
        s_per_M0.append(1-np.exp((z0-z)/y))
    return s_per_M0


data = np.loadtxt('abundanceTable.txt').T
#convert to Z
metalGCS = [0]
metalGCS.extend(10**data[0])

#normalize data and use cumulative sum
fractionGCS = [0]
fractionGCS.extend(np.cumsum(data[1]/np.sum(data[1])))

#plot
y = 0.5
z0 = 0.0

fig, ax = plt.subplots(1,1)
ax.plot(metalGCS,closedBoxFrac(metalGCS,z0,y),label=r'$\mathrm{SCB},\ y=%.2g,\ Z_0=%.2g$' %(y,z0))
ax.plot(metalGCS,fractionGCS,label='GCS data', ls='--', c='k')
ax.set_xlabel(r'$Z$')
ax.set_ylabel(r'$s/M_0$')
ax.set_xlim([0,3])
ax.set_ylim([0,1])
ax.legend()
fig.tight_layout()
#plt.show()
fig.savefig('2e.pdf')