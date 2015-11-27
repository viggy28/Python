counts = dict()  
names = ['csev','owen','csev','zqian','cwen']  
print names
for name in names:  
    print name
    counts[name] = counts.get(name,0) + 1  
print counts 