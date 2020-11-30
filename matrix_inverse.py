#!/usr/bin/env python
# coding: utf-8

def main():

    # In[21]:
    from sys import argv
    N = 2**(int(argv[1]))




    import dask.array as da


    # In[22]:


    from dask.distributed import Client
    client = Client()
    client


    # In[30]:


    x = da.random.random(size=(N,N))


    # In[31]:


    prod = da.linalg.inv(x)


    # In[32]:


    prod.compute()


    # In[25]:


    import numpy as np


    # In[ ]:





    # In[29]:


    prod.compute().shape


    # In[26]:


    np.save('tmp', prod.compute())


# In[ ]:

if __name__=='__main__':
    main()




