filenames = ['basophil.edgelist', 'blood_platelet.edgelist', 'eosinophil.edgelist', 'mast_cell.edgelist', 'monocyte.edgelist', 'neutrophil.edgelist']
#filenames = ['b.edgelist']
count = 1
for fname in filenames:
    ofile = open('new' + fname, 'w')
    infile = open(fname, 'r')
    for line in infile:
        line=str(line)
        line=line.strip()
        s=str(count)
        s=s+" "
        s=s+str(line)+" 1"
        s=s+"\n"
        #print(s)
        ofile.write(s)
        #ofile.write(" 1")
        
    count = count + 1