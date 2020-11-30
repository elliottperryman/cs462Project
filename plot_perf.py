import numpy as np
import matplotlib.pyplot as plt
from os import system
from sys import argv

max_exp = 12
times = np.arange(1,max_exp).reshape(1,-1)

for N in [1,2]:
    system('rm out.txt scheduler.json junk.* *.npy')
    system('mpirun --oversubscribe --np '+str(N+1)+' dask-mpi --no-nanny --scheduler-file scheduler.json &')
    for exp in range(1,max_exp):
        print('time -f "%e" -a -o out.txt python '+argv[1]+' '+str(exp))
        system('time -f "%e" -a -o out.txt python '+argv[1]+' '+str(exp))
    # kill mpirun 
    system('ps aux | grep -e "mpirun" | grep -v -e "color" > junk.txt')
    with open ('junk.txt', 'r') as file:
        data = file.read().split()[1]
        system('kill '+data)

    times = np.append(times, np.loadtxt('out.txt', delimiter='\n', dtype=float).reshape(1,-1),0)

np.save(argv[1][:-3]+'.npy', times)
