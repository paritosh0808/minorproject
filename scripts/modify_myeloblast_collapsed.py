import os

directory = "C:\\Users\\320052309\\code\\minorproject\\collapsed-dataset\\"
    
filename = "newcollapsed_myeloblast.edgelist"

f = open("C:\\Users\\320052309\\code\\minorproject\\collapsed-dataset\\newcollapsed_myeloblast.edgelist","r")
new_file = "C:\\Users\\320052309\\code\\minorproject\\collapsed-dataset\\m_" + filename 

temp = open("temp.txt","w")
lines = f.readlines()
for line in lines:
    line = line.split()
    #print(line[0] + "---" + line[1])
    string = "myeloblast_NODE__" + str(line[0]) + " myeloblast_NODE__" + str(line[1]) + "\n"
    #print(string)
    temp.write(string)
temp.close()
os.rename("temp.txt",new_file)
f.close()