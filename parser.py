import re, urllib

proxies = {'http':'http://172.21.48.1:8080/'}
myurl = urllib.urlopen('http://www.thehindu.com/', proxies=proxies).read()


#myurl = input("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl,proxies=proxies).read(), re.I):
        print i 
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i,roxies=proxies).read(), re.I):
                print ee
                textfile.write(ee+'\n')
textfile.close()