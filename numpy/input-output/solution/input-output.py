import numpy as np
import sys

filename = '../xy-coordinates.dat'
xy = np.loadtxt(filename)
xy[:,1] += 2.5
np.savetxt('new-' + 'xy-coordinates.dat', xy, fmt='%.6f', header='modified data')
