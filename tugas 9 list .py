#!/usr/bin/env python
# coding: utf-8

# In[1]:


# LIST BERURUTAN 
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
a == b


# In[2]:


a = [1, 2, 3, 4, 5]
c = [1, 2, 3, 4, 5]
a == c


# In[4]:


# List dapat berisi tipe data apapun
a = [2, 3, 5, 7]
a





# In[5]:


b = ['John', 23, True, 3.87]
b


# In[6]:


#List di dalam list (Nested list)
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m


# In[9]:


# list dengan operator + 
Bil1 = [1,2,3,]
Bil2 = [4,5,6]
bilTotal = Bil1 + Bil2
print (bilTotal)


# In[12]:


# list dengan operato *
Bil = [1,2,3,4,5]
BilTotal = [1,2,3,4,5]*2
print (BilTotal)


# In[10]:


# list dalam indeks append 
a_list = [1,2,3,4]
a_list +=[5] 
a_list 







# In[17]:


# list dalam extend
daftar1 = [10,20,30]
daftar2 = [40,50,60]
daftar1.extend(daftar2)
print(daftar1)
           


# In[18]:


#list dalam sort
angka = [10,2,3,4,6,7,8,5]
angka.sort()
print(angka)


# In[23]:


#list dalam pop
buah = ['apel','jambu','mangga']
buah.pop(1)
print(buah)


# In[25]:


# list dalam del
buah = ['apel','jambu','mangga','jeruk','pepaya']
del buah[2]
buah


# In[26]:


# list dalam remove
buah = ['apel','jambu','mangga','jeruk','pepaya']
buah.remove("jambu")
buah


# t1 = [1,2]
# t2 = t1.append(3)
# print(t1)

# In[29]:


p1 = [2,3]
p2 = p1.append(1)
print(p1)
p3 = p1 + [3]
print(p3)
p2 is p3


# In[ ]:




