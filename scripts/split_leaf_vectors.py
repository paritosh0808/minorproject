import os

directory = "C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\"
filename = "leaf_vectors.embedding"

f = open(directory + filename,"r")

basophil = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\basophil_leaf.embedding","w")
blood_platelet = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\blood_platelet_leaf.embedding","w")
eosinophil = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\eosinophil_leaf.embedding","w")
mast_cell = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\mast_cell_leaf.embedding","w")
monocyte = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\monocyte_leaf.embedding","w")
neutrophil = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\neutrophil_leaf.embedding","w")

lines = f.readlines()
for line in lines:
    if "basophil" in line:
        basophil.write(line)
    if "blood_platelet" in line:
        blood_platelet.write(line)
    if "eosinophil" in line:
        eosinophil.write(line)
    if "mast_cell" in line:
        mast_cell.write(line)
    if "monocyte" in line:
        monocyte.write(line)
    if "neutrophil" in line:
        neutrophil.write(line)
basophil.close()
blood_platelet.close()
eosinophil.close()
mast_cell.close()
monocyte.close()
neutrophil.close()
f.close()