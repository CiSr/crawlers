from BeautifulSoup import BeautifulSoup
import urllib2
url= 'http://www.espnfc.com/spi/rankings/_/view/fifa/teamId/203/mexico?cc=5901'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
rank = soup.find("div", {"class": "rank-box"}).h6.contents
rank = soup.find("div", {"class": "rank-box"}).h6.contents
teaminfo = soup.find("div", {"class": "team-info"})
name = teaminfo.h4.contents
rating = teaminfo.ul.p.span.contents
print rating
