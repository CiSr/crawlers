#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import datetime
from BeautifulSoup import BeautifulSoup


#proxies = {'http':'http://172.21.48.1:8080/'}
#sock = urllib.urlopen('http://www.thehindu.com/', proxies=proxies).read()

sock=urllib.urlopen("http://www.thehindu.com/")
htmlSrc=sock.read()
soup=BeautifulSoup(htmlSrc)
print "The Hindu\n"
today = datetime.date.today()
print today.strftime('The date %d, %b %Y')

print "\t\t****Flash news****"

for div in soup.findAll('div', attrs={'class':'v-overlay'}):
    
    #for data in div.findNextSibling('div', attrs={'class':'data'}):
    print div.text

    for data in soup.findAll('p' ,attrs={'class' :'lead-text'}):

	print data.text
	#print "\n"
#print "\n"
#print "Bulletin News\n"


#for div in soup.findAll('div',attrs={'class':'sm-overlay'}):
		
#	print div.text	
#	print "\n\t"

print "\n"
#for div in soup.findAll('div',attrs={'class':'one-column-vertical clearfix'}):
#	for div in a.findAll('a',attrs={'href'}):
#		print a.text
	
for div in soup.findAll('div',attrs={'class':'v-overlay'}):
	for p in div.findAll('p',attrs={'class':'lead-text'}):
        	print p.text


