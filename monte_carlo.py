#!/usr/bin/env python
# coding: utf-8

def main():
    # In[1]:
    from sys import argv
    import numpy as np
    import dask.array as da


    # In[2]:
    from time import time

    from dask.distributed import Client
    client = Client(n_workers=int(argv[1]), threads_per_worker=2, dashboard_address=None, scheduler_port=0)
    print(client)


    # In[6]:
    times = []
    for exp in range(1,31):
        N = 2**exp
        t1 = time()
        x = da.random.random(size=(2,N))*2 -1
        pi = (4.*(x[0]**2 + x[1]**2 < 1.).sum()/N).compute()
        print('exp:',exp,'\t N:',N,'\t pi:',pi,'\t err:',np.abs(pi-np.pi))
        t2 = time()
        print('time: ',t2-t1)
        times.append(t2-t1)

if __name__=='__main__':
    main()

