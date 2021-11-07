#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import nltk
nltk.download('stopwords')
nltk.download('punkt')


# In[4]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import string
import copy
import pickle


# In[11]:


title = "20_newsgroups"
os.chdir("C:/Users/Razer/Downloads/20_newsgroups")
paths = []
for (dirpath, dirnames, filenames) in os.walk(str(os.getcwd())+'/'+title+'/'):
    for i in filenames:
        paths.append(str(dirpath)+str("/")+i)

print(dirpath)


# In[12]:


paths[0]


# In[14]:


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words:
            new_text = new_text + " " + w           
    return np.char.strip(new_text) 


# In[17]:


def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
    data = np.char.replace(data, " ", " ")
    data = np.char.replace(data, ',', '')
    return data 


# In[18]:


def convert_lower_case(data):
    return np.char.lower(data)


# In[19]:


def stemming(data):
    stemmer= PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return np.char.strip(new_text) 


# In[20]:


def convert_numbers(data):
    data = np.char.replace(data, "0", " zero ")
    data = np.char.replace(data, "1", " one ")
    data = np.char.replace(data, "2", " two ")
    data = np.char.replace(data, "3", " three ")
    data = np.char.replace(data, "4", " four ")
    data = np.char.replace(data, "5", " five ")
    data = np.char.replace(data, "6", " six ")
    data = np.char.replace(data, "7", " seven ")
    data = np.char.replace(data, "8", " eight ")
    data = np.char.replace(data, "9", " nine ")
    return data


# In[24]:


def remove_header(data):
    try:
        ind = data.index('\n\n')
        data = data[ind:]
    except:
        print("No Header")
    return data


# In[25]:


def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


# In[27]:


def remove_single_characters(data):
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if len(w) > 1:
            new_text = new_text + " " + w
    return np.char.strip(new_text)


# In[29]:


def preprocess(data, query):
    if not query:
        data = remove_header(data)
    # lower case function
    # convert numbers
    # remove punctuation
    # remove stop words
    # remove apostrophe
    # remove single characters
    # stemming

    return data 


# In[ ]:




