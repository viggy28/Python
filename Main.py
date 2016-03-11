from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import date,timedelta
import urllib2
import csv
from _ast import With
#from methods import getPageSource, saveData, parseData1,getCategory

def main():
    
            driver = webdriver.Firefox()
    #driver.get("http://www.amazon.com/Quieting-Your-Heart-6-Month-Bible-Study/dp/0995056706/ref=zg_bsnr_books_3")
            driver.get("http://amazon.com/")
              
              
            try:
                html = driver.page_source
                  
            except:
                print "\nError: in HTML get page source!"
            print "soup1"
            soupa= BeautifulSoup(html,"html.parser")
              
            categories1=soupa.find("a",{"id":"nav-link-shopall"})
            #print categories
            print "by id"
            print categories1
            categories1.get
            caturl=categories1.get('href')
            print caturl
            categoriesurl="http://amazon.com"+caturl
            print "categoriesurl"
            print categoriesurl
              
            driver.get(categoriesurl)
            try:
                htmlb = driver.page_source
            except:
                print "error in the HTML source"
            soupb = BeautifulSoup(htmlb,"html.parser")
            #print soupb
            #soupb1 = soupb.encode("utf-8")
            print "crossed soupb1"
            categories2= soupb.encode("utf-8")
            time.sleep(2)
            categories2=soupb.find_all(attrs={"class":"nav_a"})
            time.sleep(1)
            print "categories2"
            print categories2
            #catlist = categories2.Text
            booksurl=''
            for cat in categories2:
                    #print cat.text
                if cat.text == "Books" :
                    bookurl = cat.get('href')
                    #print bookurl
                    booksurl = "http://amazon.com" + bookurl
                    print booksurl
            driver.get(booksurl)
              
            try:
                htmlc = driver.page_source
            except:
                print "Error in html source"
                  
            soupc = BeautifulSoup(htmlc,"html.parser")
            morebooks = soupc.find_all("a",{"class":"a-link-emphasis"}) 
            for morebook in morebooks :
                if morebook.text == "See all hot new releases in Books" :
                    morebookurl = morebook.get('href')
                    time.sleep(1)
            n = 1 
            while n<5:      
                if n == 1:
                    print "page number"
                    print n    
                    morebooksurl = "http://amazon.com" + morebookurl
                    print "url"
                    print morebooksurl
                    driver.get(morebooksurl)
                    n = n+1
                else:
                    print "page number"
                    print n 
                    morebooksurl = "http://amazon.com" + morebookurl + "#"+str(n) 
                    print "url"
                    print morebooksurl
                    driver.get(morebooksurl)
                    n = n+1
                    time.sleep(1)
                try:
                    htmld = driver.page_source
                    print "htmld"
                except:
                    print "error in html source"
                
#                 htmld = driver.page_source 
                soupd = BeautifulSoup(htmld,"html.parser")
                eachpagebook = soupd.find_all(attrs={"class":"zg_itemImageImmersion"})
                print "eachpage book"
                print eachpagebook
                print "fuck you"
                bno = 1 
                 
                for eachbook in eachpagebook :
                    eachpagebookurl = eachbook.find('a')['href']
                      
                    eachpagebookperurl = eachpagebookurl[21:]
                    driver.get(eachpagebookperurl)
             
                    time.sleep(2)
              
            #driver.get("http://www.amazon.com/Doctor-Coloring-Price-Stern-Sloan/dp/0399542299/ref=zg_bsnr_books_8/175-3691880-5546810")         
                    try:
                        htmle = driver.page_source
                    except:
                        print "error in html source"
                              
                    soupe = BeautifulSoup(htmle,"html.parser")
                    
                    booknname = soupe.find("span",{"id":"productTitle"})
                    print bno
                    
                    print "bookname"
                    bookname = booknname.text.encode('ascii','ignore')   #bookname
                    print bookname
                    
                    authors = soupe.find_all("a",{"class":"a-link-normal contributorNameID"})
                    #print authors
                    print "author name"
                    authornamelist= []
                    for author in authors:
       
                    
                        
                        authorname = author.text.encode('ascii','ignore')
                    
                        authornamelist.append(authorname)
                    if not authornamelist:
                        authornamelist.append("No Author")
                    print authornamelist
                    bookratings = soupe.find_all("a",{"class":"a-link-normal a-text-normal product-reviews-link"})
                    print "bookratings"
                    print bookratings
                    rating = "No rating"
                    if bookratings == None: 
                        
                        print "No ratings so far"  
                        
                         
                    else:
                        for bookrating in bookratings:
                            print "inside bookratings else part"
                            rating = bookrating.get('title').encode('ascii','ignore')
                            print rating
            
                    bookdetails = soupe.find_all("table",{"id":"productDetailsTable"})        
                    for bds in bookdetails:
                        bookdetail = bds.find_all(attrs={"class":"content"})
                      
                    for bd in bookdetail:
                        
                        eachbookdet = bd.find_all('li')
                        print eachbookdet
                    
                    moredetailslist = []   
                    i = 0
                    for b in eachbookdet:
                        if i < 6:
                            moredetails = b.text.strip()
                            if i == 0:
                                
                                serieslist = moredetails.split(":")
                                booktype = serieslist[0]
                                if booktype == "Series":
                                    i = i+1
                                    continue
                                else:
                                    moredetailslist.append(moredetails)
                                    print moredetailslist
                                    i = i+1   
                            else: 
                                moredetailslist.append(moredetails)
                                print moredetailslist
                                i = i+1   
                    print "booktype"
                    moredetailslist[0]
                    print "publisher"          
                    print moredetailslist[1]
                    print "language"
                    print moredetailslist[2]
                    print "isbn"
                    print moredetailslist[3]            
                    moredetailslist = [s.split(':')[1] for s in moredetailslist]               
                    #print outlist
                     
                    with open ("booklist1.csv","a") as filewriter:
                      
                        if bno == 1:
                            filewriter.write("Bookname"+"\t"+"Authorname"+"\t"+"Book Pages"+"\t"+"Publisher"+"\t"+"Language"+"\t"+"ISBN-10"+"Rating\n")
                              
                            filewriter.write(bookname+"\t"+authornamelist[0]+"\t" + moredetailslist[0]+"\t"+moredetailslist[1]+"\t" + moredetailslist[2]+"\t"+moredetailslist[3]+"\t" +rating+"\n")
                            bno = bno+1
                        else:
                            filewriter.write(bookname+"\t"+authornamelist[0]+"\t" + moredetailslist[0]+"\t"+moredetailslist[1]+"\t" + moredetailslist[2]+"\t"+moredetailslist[3]+"\t" +rating+"\n")
              
                
        
        
        
if __name__ == '__main__':
    main()  