#!/usr/bin/env python
# coding: utf-8

def main():
    # In[11]:
    from sys import argv

    import dask.array as da
    
    from time import time

    from dask.distributed import Client
    client = Client(n_workers=int(argv[1]), threads_per_worker=2, dashboard_address=None, scheduler_port=0)
    print(client)

    for exp in range(1,13):
        N = 2**exp
        t1 = time()
        x = da.random.random(size=(N,N))
        z = da.linalg.inv(x).compute() 
        t2 = time()
        print('exp:',exp,'\t N:',)
        print('time: ',t2-t1)


if __name__=='__main__':
    main()

