#!/usr/bin/env python
# coding: utf-8

# # Ejemplos de conjuntos
# 

# In[1]:


set(['ANA','Ana','ana'])


# In[4]:


conjunto={'ANA', 'Ana', 'ana'}


# In[5]:


type(conjunto)


# # Practica

# In[9]:


erick=set(['carlos','juan','maria','pedro','miguel'])
wife=set(['cindy','juan','miguel'])
blacklist=set(['ana','sofia','carlos'])


# In[10]:


#invitados en comun
erick & wife


# In[15]:


#excluidos
(erick- wife) & blacklist


# In[18]:


#invitados originalmente 
erick | wife


# In[19]:


#lista final de invitados

(erick|wife)- blacklist


# In[22]:


def returnNoMatches(a,b):
    a=set(a)
    b=set(b)
    return[list(b-a),list(a-b)]


# In[23]:


returnNoMatches(erick,wife)


# In[ ]:




