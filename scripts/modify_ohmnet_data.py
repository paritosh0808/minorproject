import os

directory = "C:\\Users\\320052309\\code\\minorproject\\blood-data-ohmnet\\edgelists\\"

for filename in os.listdir(directory):
    f = open(directory + filename,"r")
    new_file = "C:\\Users\\320052309\\code\\minorproject\\blood-data-ohmnet\\edgelists\\m_" + filename 
    
    temp = open("temp.txt","w")
    lines = f.readlines()
    for line in lines:
        line = line.split()
        #print(line[0] + "---" + line[1])
        string = "data_edgelists_" + filename + "__" + str(line[0]) + " data_edgelists_" + filename + "__" + str(line[1]) + "\n"
        #print(string)
        temp.write(string)
    temp.close()
    os.rename("temp.txt",new_file)
    f.close()