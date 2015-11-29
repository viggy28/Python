ls=list()
dic=dict()
fname=raw_input("Enter the file name")
fhandle=open(fname)
for line in fhandle:
    line=line.rstrip()
    count=0
    if line.startswith('From '):
        
        for word in line.split():
            count=count+1
            if count == 6 :
                hrcount=0
                for hr in word.split(':'):
                    hrcount=hrcount+1
                    if hrcount%3==1:
                        ls.append(hr)
for hr in ls:
    dic[hr]=dic.get(hr,0)+1
#print dic
ls=dic.items()
#print ls
ls.sort(cmp=None, key=None, reverse=False)

for hr,tim in ls:
    print hr, tim
                
                