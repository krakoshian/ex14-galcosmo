import numpy as np
import collections
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font',family = 'serif', size=15)

def accretingBoxFrac(Z, y):
    if not isinstance(Z, collections.Iterable):
        Z = [Z]
    s_per_M0 = []
    
    for z in Z:
        s_per_M0.append(1/(1 - 1/np.log(1-(z/y))))
    return s_per_M0
    
    
data = np.loadtxt('abundanceTable.txt').T
#convert to Z
metalGCS = [0]
metalGCS.extend(10**data[0])

#normalize data and use cumulative sum
fractionGCS = [0]
fractionGCS.extend(np.cumsum(data[1]/np.sum(data[1])))


#plot
Y = [0.4, 0.6, 0.8]
fig, ax = plt.subplots(1,1)
for y in Y:
    ax.plot(metalGCS,accretingBoxFrac(metalGCS, y),label=r'$\mathrm{ABM},\ y=%.2g$' %(y))
ax.plot(metalGCS,fractionGCS,label='GCS prediction',ls='--', c='k')
ax.set_xlabel(r'$Z$')
ax.set_ylabel(r'$s/M$')
ax.set_xlim([0,3])
ax.set_ylim([0,1])
ax.legend()
fig.tight_layout()
#plt.show()
fig.savefig('3b.pdf')
