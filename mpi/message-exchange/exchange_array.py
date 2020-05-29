# mpiexec -n 2 python3 exchange_array.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD # communicator object containing all processes
size = comm.Get_size()
rank = comm.Get_rank()

data = np.empty(100000, dtype=int)
data[:] = rank
bfr = np.empty(100000, dtype=int)

# using combined send and receive
if rank == 0:
    src, tgt = 1,1
else:
    src, tgt = 0, 0

comm.Sendrecv(data, dest=tgt, recvbuf=bfr, source=src)

print('Rank %d received array from rank %d' % (rank, bfr[0]))