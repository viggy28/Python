

emailslst=list()
emails=''
fname=raw_input("Enter the filename")
fhandle=open(fname)
for line in fhandle:
    line=line.rstrip()
    if line.startswith('From '):
        
    #    emailslst.append(line[6:])
        word=''
        count=0
        #print "nextline--------------"
        #print line
        count=0
        for word in line.split():
            count=count+1
            if count==2:
                #print word  
                emailslst.append(word)
                
        
              
        
#print emailslst
users=dict()
for name in emailslst: 
    #print name 
    users[name] = users.get(name,0) + 1  
#print users 
#print users.items()
maxsend='None'
maxcount=0
for sender,count in users.items():
    #print "insideloop"
    #print sender,count
    
    if maxsend is None or maxcount<count:
        #print "insideif"
        maxsend=sender
        maxcount=count
print maxsend,maxcount
    
    

    

