infile = open('embeddings\\collapsed\\deepwalk\\collapsed.embeddings','r')
outfile1 = open('embeddings\\collapsed\\deepwalk\\tsvector.tsv','w')
outfile2 = open('embeddings\\collapsed\\deepwalk\\tsmetadata.tsv','w')
infile.readline()
for line in infile:
    linelist = []
    linelist =  line.split(" ")
    meta = linelist[0] + '\n'
    outfile2.write(meta)
    del linelist[0]
    str1 = '\t'
    str1 = str1.join(linelist)
    outfile1.write(str1)
    