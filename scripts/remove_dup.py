lines_seen = set()
duplines = set()
ofile = open('collapsed.edgelist', 'w')
infile = open('combined.edgelist', 'r')
for line in infile:
    if(line not in lines_seen):
        ofile.write(line)
        lines_seen.add(line)
    elif(line in lines_seen):
        duplines.add(line)
ofile.close()
#print(duplines)
leng1 = len(duplines)
leng2 = len(lines_seen)
#print(leng1)
#print(leng2)
print("Edgelist collapsed") 


