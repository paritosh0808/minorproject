import os

directory = "C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\"
filename = "internal_vectors.embedding"

f = open(directory + filename,"r")

mb = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\myeloblast_internal_vectors.embedding","w")
md = open("C:\\Users\\320052309\\code\\minorproject\\embeddings\\ohmnet\\myeloid_internal_vectors.embedding","w")

lines = f.readlines()
for line in lines:
    if "myeloblast" in line:
        mb.write(line)
    if "myeloid" in line:
        md.write(line)
mb.close()
md.close()
f.close()