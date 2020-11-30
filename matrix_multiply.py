#!/usr/bin/env python
# coding: utf-8

def main():
    # In[11]:
    from sys import argv
    N = 2**(int(argv[1]))

    import dask.array as da

    from dask.distributed import Client
    client = Client(scheduler_file='./scheduler.json')

    x = da.random.random(size=(N,N))
    y = da.random.random(size=(N,N))

    prod = x.dot(y)

    import numpy as np


    np.save('tmp', prod.compute())


if __name__=='__main__':
    main()
else:
    print(__name__)

