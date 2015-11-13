#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import datetime
from BeautifulSoup import BeautifulSoup
import sys


f = open("urls.txt")
start_urls = [url.strip() for url in f.readlines()]
f.close()




#url_list=raw_input("Enter the urls:")

for i in range(0,4):
	temp=start_urls[i]
	sock=urllib.urlopen(temp)
	htmlSrc=sock.read()
	soup=BeautifulSoup(htmlSrc)

	print "Moto g-phones"

	for div in soup.findAll('div', attrs={'class':'coming-soon-text'}):
    		print div.text

	print "Price:"

	for span in soup.findAll('span', attrs={'class':'selling-price omniture-field'}):
    	#	print "\n"
    		print span.text

	print "Specifications in Moto-G"
	#<div class="productSpecs specSection">

	for div in soup.findAll('div', attrs={'class':'productSpecs specSection'}):
    		print div.text
    		print "\n"
