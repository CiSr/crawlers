#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import datetime
from BeautifulSoup import BeautifulSoup
import re
sock=urllib.urlopen("http://www.thehindu.com/")
htmlSrc=sock.read()
soup=BeautifulSoup(htmlSrc)
print "The Hindu\n"
today = datetime.date.today()
print today.strftime('The date %d, %b %Y')

print "\t\t****Flash news****"


celex = soup.find('h1')

temp=celex.renderContents()

print temp



for p in soup.findAll('p',attrs={'class':'lead-text'}):
    print p.text