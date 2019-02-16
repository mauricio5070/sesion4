#!/usr/bin/env python
# coding: utf-8

# # Diccionarios
# 

# In[73]:


#agenda telefonica

agenda= {
    'Juan': 88565233,
    'Carlos':78456235
}


# In[3]:


agenda['Carlos']


# In[4]:


agenda['Maria']=911


# In[5]:


agenda


# In[6]:


agenda.get('Juan','no lo tengo!!1')


# In[8]:


agenda.get('Sofia','no lo tengo!!!')


# In[9]:


del agenda ['Maria']


# In[10]:


agenda


# In[79]:


agenda['Laura']=88476792


# In[80]:


agenda


# # Listar las llaves de un diccionario

# In[14]:


#Consulta de una llave en especifico
list(agenda)


# In[15]:


'Juan' in agenda


# In[16]:


'Maria' in agenda


# In[17]:


'Juan' not in agenda


# In[19]:


#Lista de tuplas

dict([('Juan',88565233), ('Carlos', 78456235), ('Laura', 8847679)])


# In[20]:


dict(pepe=1,juan=2,carlos=3)


# In[21]:


knights={'Gallahad':'the pure','Robbin':'the brave'}


# In[22]:


[i for i in knights]


# In[23]:


[i for i in knights.items()]


# In[39]:


a=['A','B','C']
b=['a','b','c']


# In[30]:


dict(zip(a,b))


# In[40]:


a.append('Z')


# In[41]:


a


# In[42]:


dict(zip(a,b))


# In[43]:


b.append('z')


# In[44]:


dict(zip(a,b))


# In[45]:


# diccionario.update(llave: valor)


# In[46]:


agenda


# In[47]:


agenda_2={'sofia':73747394, 'Pepe':8282382}


# In[81]:


new_agenda=agenda.copy()
new_agenda.update(agenda_2)


# In[82]:


new_agenda


# In[83]:


z=dict(**agenda,**agenda_2)


# In[84]:


z


# In[ ]:




