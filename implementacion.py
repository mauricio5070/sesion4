#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creacion de un bloque de diccionarios


# In[2]:


def caminar():
    print('Estoy caminando')


# In[3]:


def correr():
    print('Estoy corriendo')


# In[4]:


def mirar():
    print('Estoy mirando')


# In[5]:


s={'caminar':caminar,'correr':correr,'mirar':mirar}


# In[7]:


s


# In[13]:


s['correr']


# In[9]:


a= s['mirar']


# In[11]:


a()


# In[14]:


s['caminar']()


# In[ ]:




