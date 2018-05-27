#downloads pdfs indexed by google
#input:no of pages to search & query
#generates a log file


from urllib.request import urlopen
import re
import urllib
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import urllib.request
from urllib.parse import unquote
import os
import sys
from datetime import datetime
timee=str(datetime.now())
b=0
tx = open('log.txt','wb')
timenow=timee.encode('utf-8')
tx.write(timenow)
keyword=input('Enter search term :')
try:
    nodown =int(input('Enter no of pdf\'s to be downloaded :'))
except ValueError:
    print("Not a number")
query=keyword.replace(' ','+')
name=keyword.replace(' ', '_')
query=query+'+pdf'
page=[0,10,11,21,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191]
try:
	os.makedirs(name)
except:
	pass
pageno=15
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
for k in range(1,pageno):
	pageid=page[k]
	link = 'https://www.google.com/search?q=filetype%3Apdf+'+ query +'&start='+str(pageid)
	#print(link)
	headers={'User-Agent':user_agent,} 
	request=urllib.request.Request(link,None,headers)
	html = urllib.request.urlopen(request)
	soup = BeautifulSoup(html,'lxml')
	po=soup.find_all(href=re.compile("http://"))
	newlin='\n'
	newline=newlin.encode('utf-8')
	tx.write(newline)
	done=0
	for i in po:
		if(done>=nodown):
			exit()
		io=i.encode('utf-8')
		searchObj = re.search( r':https://(.*).pdf', str(io), re.M|re.I)
		searchObj1 = re.search( r':http://(.*).pdf', str(io), re.M|re.I)
		if searchObj:
			hulu=searchObj.group(1)
			cbmuth=hulu.encode('utf-8')
			pdflink = re.search( r'b\'(.*)%252Bfiletype(.*)%2', str(cbmuth), re.I)
			dracu= 'http://'+pdflink.group(1)
			drink= dracu.encode('utf-8')
			realink1=urllib.parse.unquote(dracu)
			realink2=urllib.parse.unquote(realink1)
			realink=urllib.parse.unquote(realink2)
			split = urlsplit(str(drink))
			filename = split.path.split("/")[-1]
			
		
			titleg = re.search( r'(.*).pdf', filename, re.M|re.I)
			if(titleg==None):
				b=b+1
				title5='notitle'+ str(b)+'.pdf'
			else:		
				title5 = titleg.group(1)+'.pdf'
			title= title5.encode('utf-8')
		
			titlee=str(name)+'/'+str(title5)
			
			#fullfilename = os.path.join(myPath, )

			
			try:
				
				filoo = urllib.request.urlretrieve (realink,titlee)
				tx.write(drink)
				tx.write(newline)
				tx.write(title)
				tx.write(newline)
				done=done+1
				print(realink)
			except:
				pass
		if searchObj1:
			hulu1=searchObj1.group(1)
			cbmuth1=hulu1.encode('utf-8')
			pdflink1 = re.search( r'b\'(.*)%252Bfiletype(.*)%2', str(cbmuth1), re.M|re.I)
			dracu1= 'http://'+pdflink1.group(1)
			drinku1= dracu1.encode('utf-8')
			realink1=urllib.parse.unquote(dracu1)
			realink2=urllib.parse.unquote(realink1)
			realink=urllib.parse.unquote(realink2)
			
		

			split1 = urlsplit(str(drinku1))
			filename1 = split1.path.split("/")[-1]
			titleg1 = re.search( r'(.*).pdf', filename1, re.M|re.I)
			title12 = titleg1.group(1)+'.pdf'
			title1=title12.encode('utf-8')
			titlee=str(name)+'/'+str(title12)
			
			try:
				filoo1 = urllib.request.urlretrieve (realink,titlee)
				tx.write(title1)
				tx.write(newline)
				tx.write(drinku1)
				tx.write(newline)
				print(realink)
				done=done+1
			except:
				pass
		
#thankyou
