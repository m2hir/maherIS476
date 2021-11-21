#!/usr/bin/env python
# coding: utf-8

# In[11]:


from __future__ import print_function
from nltk.metrics import *

Sentence1='There are many similarity measures used in NLTK package'.split()
Sentence2='There are many similarity measures are avaliable in NLTK '.split()

print('Accuracy = ',accuracy(Sentence1,Sentence2))
print (Sentence1)
print (Sentence2)


# In[20]:


print(precision(set(Sentence1),set(Sentence2)))


# In[21]:


print(recall(set(Sentence1),set(Sentence2)))


# In[17]:


import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

array = confusion_matrix(Sentence1, Sentence2)
setA = set(Sentence1)
setB = set(Sentence2)
dictionary = setA.union(setB)




df_cm = pd.DataFrame(array,index= dictionary, columns = dictionary )

plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})


# In[13]:


classification_report = classification_report(Sentence1, Sentence2)

print('Classification Report \n', classification_report)


# In[31]:


from _future_ import print_function
def _edit_dist_init(len1, len2):
    lev = []
    for i in range(len1):
        lev.append([0] * len2) # initialize 2D array to zero
    for i in range(len1):
        lev[i][0] = i # column 0: 0,1,2,3,4,...
    for j in range(len2):
        lev[0][j] = j # row 0: 0,1,2,3,4,...
    return lev

def _edit_dist_step(lev,i,j,s1,s2,transpositions=False):
    c1 =s1[i-1]
    c2 =s2[j-1]
   # skipping a character in s1
    a =lev[i-1][j] +1
  # skipping a character in s2
    b =lev[i][j -1]+1
  # substitution
    c =lev[i-1][j-1]+(c1!=c2)
  # transposition
    d =c+1 # never picked by default
    if transpositions and i>1 and j>1:
    if s1[i -2]==c2 and s2[j -2]==c1:
        d =lev[i-2][j-2]+1
      # pick the cheapest
    lev[i][j] =min(a,b,c,d)


def edit_distance(s1, s2, transpositions=False):
  # set up a 2-D array
    len1 = len(s1)
    len2 = len(s2)
    lev = _edit_dist_init(len1 + 1, len2 + 1)
  # iterate over the array
    for i in range(len1):
    for j in range(len2):
        _edit_dist_step(lev, i + 1, j + 1, s1, s2,transpositions=transpositions)
    
    return lev[len1][len2]

   
    
edit_distance("relate","relation")
        


# In[ ]:




