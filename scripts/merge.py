filenames = ['basophil.edgelist', 'blood_platelet.edgelist', 'eosinophil.edgelist', 'mast_cell.edgelist', 'monocyte.edgelist', 'neutrophil.edgelist']
with open('combined.edgelist','w') as ofile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                ofile.write(line)

print("Combined edgelist created")



