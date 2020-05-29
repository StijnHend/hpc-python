# mpiexec -n 4 python3 helloworld.py
# install packages: mpich, openmpi-bin

from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator object containing all processes

size = comm.Get_size()
rank = comm.Get_rank()

print("I am rank %d in group of %d processes" % (rank, size))