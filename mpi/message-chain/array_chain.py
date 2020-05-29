# mpiexec -n 5 python array_chain.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD # communicator object containing all processes
size = comm.Get_size()
rank = comm.Get_rank()

N = 100
data = np.full(N, rank, int)
bfr = np.empty(N, dtype=int)

# using combined send and receive
tgt = rank + 1
src = rank - 1
if rank == 0:
    src = MPI.PROC_NULL
if rank == size - 1:
    tgt = MPI.PROC_NULL

comm.Sendrecv(data, dest=tgt, recvbuf=bfr, source=src)

if rank < size-1:
    print('Rank %d sent array to rank %d' % (rank, tgt))
if rank > 0:
    print('Rank %d received array of length %d from rank %d' % (rank, len(bfr), bfr[0]))