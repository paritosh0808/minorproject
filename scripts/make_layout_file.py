#!/usr/bin/env python
# coding: utf-8

# In[5]:


import networkx as nx
import os


# In[6]:


directory = "C:\\Users\\320052309\\code\\minorproject\\blood-data-ohmnet\\edgelists\\"
new_path = "C:\\Users\\320052309\\code\\minorproject\\muxviz data\\Layouts\\"


# In[8]:


for filename in os.listdir(directory):
    print(os.path.join(directory, filename))
    dataset = open(os.path.join(directory, filename),"rb")
    G=nx.read_edgelist(dataset)
    nodelist = list(G.nodes)
    #print(nodelist)
    new_file = filename.replace(".edgelist",".txt")
    f = open(new_path + new_file,"w")
    for i in nodelist:
        line = str(i) + " G_" + str(i) + "\n"
        f.write(line)


# In[ ]:




