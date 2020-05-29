# mpiexec -n 5 python reduce.py
from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10 * size, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)

n = comm.reduce(rank, op=MPI.SUM, root=0) # returns the value
# sums the values of the rank of all processes
print(n)

comm.Reduce(data, buffer, op=MPI.SUM, root=0) # in-place modification
# contains the elementwise sum of the data vectors
print(data)
print(buffer)