# mpiexec -n 2 python3 exchange.py
from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator object containing all processes

size = comm.Get_size()
rank = comm.Get_rank()

dict = {'rank': rank}

# using separate send and receive
# if rank == 0:
#     recv_dict = comm.recv(source=1)
#     comm.send(dict, dest=1)
# else:
#     comm.send(dict, dest=0)
#     recv_dict = comm.recv(source=0)

# using combined send and receive
if rank == 0:
    src, tgt = 1,1
else:
    src, tgt = 0, 0

recv_dict = comm.sendrecv(dict, dest=tgt, source=src)

print('Rank %d received message from rank %d' % (rank, recv_dict.get('rank')))