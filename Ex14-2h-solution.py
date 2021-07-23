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
metalHalo = [0]
metalHalo.extend(10**data[2])

#normalize data and use cumulative sum
fractionHalo = [0]
fractionHalo.extend(np.cumsum(data[3]/np.sum(data[3])))

#plot
y = 0.035
z0 = 0

fig, ax = plt.subplots(1,1)
ax.plot(metalHalo,closedBoxFrac(metalHalo,z0,y),label=r'$\mathrm{SCB},\ y=%.2g,\ Z_0=%.2g$' %(y, z0))
ax.plot(metalHalo,fractionHalo,label='Halo data', ls='--', c='k')
ax.set_xlabel(r'$Z$')
ax.set_ylabel(r'$s/M_0$')
ax.set_xlim([0,0.3])
ax.set_ylim([0,1])
ax.legend(loc='best')
fig.tight_layout()
#plt.show()
fig.savefig('2g.pdf')