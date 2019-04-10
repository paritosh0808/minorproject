import networkx as nx
import os
from itertools import combinations 

dataset=open("C:\\Users\\320052309\\code\\minorproject\\collapsed-dataset\\collapsed.edgelist", 'rb')
G=nx.read_edgelist(dataset)
nodelist = list(G.nodes) 

f = open("all_samples.txt","w")

comb = combinations(nodelist, 2)
#comb = combinations([1, 2, 3], 2)  

count = 0
 
# Print the obtained combinations 
for i in list(comb): 
    i = str(i)
    i = i.replace("(","")
    i = i.replace(")","")
    i = i.replace(",","")
    i = i.replace("'","",4)
    #print(i)
    count = count + 1
    f.write(i)
    f.write("\n") 

print(count)

f.close()