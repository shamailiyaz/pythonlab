#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1=[1,3,6,53, 'sun','moon']
list1


# In[4]:


list1[3]


# list1[6]

# In[5]:


list1[6]


# In[12]:


spam=[['cat,bat,rat'],[1,2,3]]
spam[0][1]


# In[9]:


spam=['cat','rat','bat']
spam[0]=[-3]


# In[10]:


spam=[1:2]


# In[14]:


spam=[['cat','bat','rat'],['1','2','3','4'],[1,3,4,4.5]]
list[2:1]


# In[16]:


list1=['shama','anju','tabbu']
list2=['1','2','3']
list1+list2


# In[ ]:


catNames =[]
while True:
    print('Enter the name of cat'+ str(len(catNames)+1) +'(or enter nothing to stop)')
    name=input()
    if name=='':
        break
        catNames=catNames+[name]# list concatenation
        print('the cat names are:')
        for name in catNames:
            print(''+name)


# In[5]:


spam=['cat','rat','bat']
for i in range(5):
    print(spam[2])
    print(i)


# In[2]:


'howdy' in ['hello','hi','howdy','heyas']


# In[1]:


spam=['hello','hi','howdy','heyas']


# In[6]:


mypets=['zophie','pooka','fat-tail']
print('Enter a pet name:')
name=input()
if name not in mypets:
    print('I do not have a pet named'+name)
else:
        print(name+ 'is my pet.')


# In[9]:


cat=['fat','gray','loud']
size=cat[0]
color=cat[1]
disposition=cat[2]
size,color,disposition


# In[10]:


supplies=['pens','staplers','flamethrowers','bindres']
for index, item in enumerate(supplies):
    print('index' + str(index)+ 'in supplies is:'+item)


# In[13]:


import random
pets=['dogs','cat','moose']
random .choice(pets)


# In[14]:


random.choice(pets)


# In[15]:


random.choice(pets)


# In[20]:


import random
people=['div','jessy','shama',]
random.shuffle(people)


# In[24]:


random.shuffle(people)
people


# In[22]:


random.choice(people)


# In[23]:


random.shuffle(people)


# In[25]:


spam=32
spam+1
spam


# In[ ]:


spam


# In[ ]:




