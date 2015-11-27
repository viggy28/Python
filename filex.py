# Use words.txt as the file name
count=0;
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh: 
    line=line.rstrip()
    for word in line.split():
        if len(word)>10 :
        
            print word
print count
        