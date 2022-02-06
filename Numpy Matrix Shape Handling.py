#!/usr/bin/env python
# coding: utf-8

# # Python 실습 IV: Vectors, matrices and multidimensional arrays, 

# In[2]:


import numpy as np


# In[3]:


x=[[1,2],[3,4]]
x


# ## Reshaping and resizing

# In[4]:


data = np.array([[1, 2], [3, 4]])


# In[11]:


# : 그 이후 모두 가지고 오너라, 슬라이싱
data[1:] 


# In[12]:


data.reshape(4)
# 4개의 array로 만들어진 벡터로 만들어 줘!


# In[13]:


y=np.arange(0,6,1)
y
# 시작값, 마지막은 끝값, 가운데 1은 디폴트


# In[14]:


y.reshape([3,2])
# 3,2로 변환했다.


# In[15]:


z=y.reshape([3,2])
z


# In[16]:


z=z.flatten()
z
# 다시 펼쳐줌


# In[17]:


z.shape


# In[18]:


z=z[:,np.newaxis]
z
# 새로운 축을 만든다, 차원이 증가함


# In[19]:


z.shape


# ## python numpy array reshaping

# In[20]:


x=np.array([0,1,2,3,4])
x


# In[21]:


y=np.stack((x,x,x), axis=0)
y


# In[22]:


y.shape


# In[23]:


y=np.stack((x,x,x), axis=1)
y


# In[24]:


y.shape


# ## Broad casting

# In[25]:


x=np.array([1,2,3,4,5])
x


# In[26]:


y=np.stack((x,x*2,x*3),axis=1)
y


# In[27]:


y.shape


# In[28]:


x.shape


# In[32]:


y/x
# shape 주의해주기


# In[33]:


x1=np.array([1,2,3])
x1.shape


# In[34]:


y/x1
# 1차원 은 가로축이 맞아야 한다.


# In[35]:


z=x[:,np.newaxis]
z


# In[36]:


z.shape


# In[37]:


y /z


# ## Concatenating

# In[38]:


z =np.array([[1,2],[3,4]])
z


# In[39]:


np.concatenate([z,z],axis=1)


# In[40]:


np.concatenate([z,z],axis=0)


# ## Matrix Operation

# In[41]:


np.array([[1,2],[3,4]]).shape


# In[42]:


np.linalg.det([[1,2],[3,4]])


# In[43]:


np.round(np.linalg.det([[1,2],[3,4]]))
#round 쓰면 조금 더 깔끔하게 나타낼 수 있음


# In[44]:


np.linalg.matrix_rank([[1,2],[3,4]])
#[1,2],[3,4]-3*[1,2]
#([1,2]
#[0,-2])


# In[45]:


X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
X, Y


# In[46]:


X*Y
#성분곱


# In[47]:


np.dot(X,Y)
#행렬곱


# In[48]:


X@Y
#행렬곱

