
# coding: utf-8

# In[10]:


import math
import csv
import random
a=[]
with open('C:\Users\Mahesh\Desktop\ESE\DM lab\md\data.csv','rb') as data:
    reader=csv.reader(data,delimiter='\t')
    data=list(reader)
length=len(data)
for i in range(length):
    a.append(list(data[i][0].split(',')))
a


# In[11]:


tup_len=len(a[0]);
tup_len
l_outcome={}
s=set()
for i in range(len(a)):
    s.add(a[i][-1]);
dis={}
for i in s:
    dis[i]=0;
for i in a:
    dis[i[-1]]+=1;
dis
l_outcome=dis;


# In[6]:


l=[]
dis={}
s=set()
for j in range(len(a[0])-1):
    dis={}
    for i in range(len(a)):
        s.add(a[i][j]);
    for i in s:
        dis[i]=[0,0];
    for x in range(len(a)):
        for i in dis.keys():
            if(i==a[x][j] and a[x][-1]=='yes'):
                dis[i][0]+=1;
            if(i==a[x][j] and a[x][-1]=='no'):
                dis[i][1]+=1;
    l.append(dis)
    s.clear();
l.append(l_outcome)
for i in l:
    print""
    print i;


# In[12]:


print "Enter codition sepreted by(',') (must be in sequence) :- "
q=raw_input().split(',');
q


# In[13]:


yes=(float(l[0][q[0]][0]*l[1][q[1]][0]*l[2][q[2]][0]*l[3][q[3]][0])/l[-1]['yes']**4)*(float(l[-1]['yes'])/ length)
no=(float(l[0][q[0]][1]*l[1][q[1]][1]*l[2][q[2]][1]*l[3][q[3]][1])/l[-1]['no']**4)*(float(l[-1]['no'])/ length)
print yes
print no


# In[14]:


if(yes>no):
    print "yes"
else:
    print "no"

