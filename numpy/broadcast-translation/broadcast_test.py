import numpy as np
import matplotlib.pyplot as plt

# np flatten vs ravel:
# ravel returns a view (whenever possible) thus entries of original array can be modified, while flatten returns a copy

# np reshaping
# option 1, change original array
# a = numpy.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (3,2)
# option 2, this returns view object if possible (a copy otherwise)
# b = a.reshape(3,2)



x = np.loadtxt('points_circle.dat')
print(x.shape)
t = np.array((2.1, 1.1))
print(t.shape)
xx = x + t
plt.plot(x[:,0], x[:,1], 'o')
plt.plot(xx[:,0], xx[:,1], 'o')
plt.show()
