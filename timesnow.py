import urllib
import datetime
from BeautifulSoup import BeautifulSoup
sock=urllib.urlopen("http://www.timesnow.tv/")
htmlSrc=sock.read()
soup=BeautifulSoup(htmlSrc)
print "The Times now\n"



for a in soup.findAll('class', attrs={'href':'[a-zA-Z,0-9;:,]*.cms'}):
	print a.text    
   
