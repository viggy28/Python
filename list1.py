listwords=list()
fname=raw_input("ENter the file name")
fhandle=open(fname)
for line in fhandle:
    line=line.rstrip()
    for word in line.split():
        if word not in listwords:
            listwords.append(word) 
            listwords.sort()
print listwords

