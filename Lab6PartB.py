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


# In[10]:


def preprocess(data, query):
    if not query:
        data = remove_header(data) 
    data = convert_lower_case(data)
    data = convert_numbers(data)
    data = remove_punctuation(data)
    data = remove_stop_words(data)
    data = remove_apostrophe(data)
    data = remove_single_characters(data)
    data = stemming(data) 
    return data 


# In[ ]:


doc = 0 
postings = pd.DataFrame()

for path in paths:
    file = open(path, 'r', encoding='cp1250')
    text = file.read().strip()
    file.close()
    preprocessed_text = preprocess(text, False)
    
    if doc % 100 == 0:
        print(doc)
        
    tokens = word_tokenize(str(preprocessed_text))
    for token in tokens:
        if token in postings:
            p = postings[token][0]
            p.add(doc)
            postings[token][0] = p 
        else:
            postings.insert(value=[{doc}], loc=0,column=token)
    doc += 1 


# In[11]:


def  generate_command_tokens(query):
    query = query.lower()
    tokens = word_tokenize(query)
    
    commands = []
    query_words = []
    
    for t in tokens:
        if t not in ['and', 'or', 'not']:
            processed_word = preprocess([t], True)
            print(str(processed_word))
            query_words.append(str(processed_word))
        else:
            commands.append(t)
            
    return commands, query_words


# In[12]:


def gen_not_tuple(query_words, commands):

    tup = []

    while 'not' in commands:

        i = commands.index('not')

        word = query_words[i]

        word_postings = get_not(word)

        tup.append(word_postings)

        commands.pop(i)

        query_words[i] = i

        print('\nAfter Not Processing:', commands, query_words)

    return tup


def binary_operations(query_words, commands, tup):

    a = postings[query_words[0]][0]

    query_words.pop(0)

    for i in range(len(commands)):

        if type(query_words[i]) == int:

            b = tup.pop(0)
        else:

            b = postings[query_words[i]][0]

        if commands[i] == 'and':

            a = a.intersection(b)
        elif commands[i] == 'or':

            a = a.union(b)
        else:

            print('Invalid Command')

    return a


def execute_query(query):

    (commands, query_words) = generate_command_tokens(query)

    tup = gen_not_tuple(query_words, commands)

    print('\nCommands:', commands)

    print('\nQuery Words:', query_words)

    print('\nTup:', len(tup))

    final_set = binary_operations(query_words, commands, tup)

    print('\nFinal Set:', final_set)

    return final_set


def print_file(file):

    out_file = open(paths[file], 'r', encoding='cp1250')

    out_text = out_file.read()

    print(out_text)


# In[ ]:




