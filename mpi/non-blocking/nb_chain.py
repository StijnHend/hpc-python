# mpiexec -n 5 python nb_chain.py
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

sendreq = comm.Isend(data, dest=tgt)
recvreq = comm.Irecv(bfr, source=src)
# Acces bfr only when the receive operation has completed, so in this case after waitall. In the mean time you can
# compute or send locally with locally available data (and also execute more Irecv operations?).

MPI.Request.waitall([sendreq, recvreq])

if rank < size-1:
    print('Rank %d sent array to rank %d' % (rank, tgt))
if rank > 0:
    print('Rank %d received array of length %d from rank %d' % (rank, len(bfr), bfr[0]))