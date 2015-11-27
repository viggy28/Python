#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
count=0
decno=0.0
chkstr="X-DSPAM-Confidence: "
fname=raw_input("Enter your file name with path")
fh=open(fname)
for line in fh:
    if not line.startswith(chkstr):
        continue
    count=count+1
#    print line
    decpos = line.find('.')
#    print decpos
    decno += float(line[decpos-1:])
avg=decno/count
print avg    
    
#print count


        





