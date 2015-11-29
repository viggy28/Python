d=dict()
l=list()
tl=list()
fname=raw_input("Enter the file name")
fhandle=open(fname)
for line in fhandle:
    line=line.rstrip()
    for word in line.split():
        l.append(word)
print "list"
print l
for name in l:
    d[name]=d.get(name,0)+1
print "dictionary"
print d 
print "list of key value pair tuples"
for key,pos in d.items():
    tl.append( (pos,key) )
print tl
print "The most common five words"
tl.sort(reverse=True) #dont try to assign that to anything

for word,no in tl[:5]:
    print word,no




#print tl[:5]
    
    
  
    
    
