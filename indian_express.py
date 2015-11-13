#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import datetime
import pprint
from BeautifulSoup import BeautifulSoup
sock=urllib.urlopen("http://indianexpress.com/")
htmlSrc=sock.read()
soup=BeautifulSoup(htmlSrc)
print "The Indian express\n"
today = datetime.date.today()
print today.strftime('The date %d, %b %Y')

print "\t\t****Flash news****"

for div in soup.findAll('div', attrs={'class':'container'}):
    
    #for nerdata in div.findNextSibling('div', attrs={'class':'data'}):
    print div.text
    print "\n"	
    #for data in soup.findAll('p' ,attrs={'class' :'lead-text'}):

	#print data.text
	#print "\n"
#print "\n"
#print "Bulletin News\n"


#for div in soup.findAll('div',attrs={'class':'sm-overlay'}):
		
#	print div.text	
#	print "\n\t"

print "\n"
for div in soup.findAll('div',attrs={'class':'left-part'}):
#	for div in a.findAll('a',attrs={'href'}):
	print div.text
	print "\n"
	

