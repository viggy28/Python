
emaillist=list()
fname=raw_input("Enter the file name")
fhandle=open(fname)
pos=0
for line in fhandle:
    line=line.rstrip()
    if line.startswith('From '):
        word=line.split()
        pos=pos+1
        print word[1]
print "There were", pos, "lines in the file with From as the first word"    