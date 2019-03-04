filenames = ['newbasophil.edgelist', 'newblood_platelet.edgelist', 'neweosinophil.edgelist', 'newmast_cell.edgelist', 'newmonocyte.edgelist', 'newneutrophil.edgelist']
with open('newcombined.edgelist','w') as ofile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                ofile.write(line)

print("Combined edgelist created")



