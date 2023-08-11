'''
to run:
 mpirun -n 2 --hosts hp1 python main.py
'''
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
name = MPI.Get_processor_name()

sys.stdout.write("Hello from hp1\n")
sys.stdout.write(f"Name: {name}  Rank {comm.rank}\n")
