from bs4 import BeautifulSoup
import urllib
from urllib.request import  urlopen
import requests
import re

def getLinks(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    count = 0
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        #links.append(link.get('href'))
        links.append(link.get('href'))
        count +=1

    print("No.of.Links",count)
    return links


links = ["https://www.cancer.gov/", "https://www.cdc.gov/cancer/","https://www.cancer.org/cancer/all-cancer-types.html", "https://www.cancer.net/navigating-cancer-care/cancer-basics/what-cancer","https://www.cancercenter.com/cancer-types","https://medlineplus.gov/cancer.html","https://www.medicalnewstoday.com/articles/323648.php","https://www.who.int/health-topics/cancer#tab=tab_1","https://www.who.int/news-room/fact-sheets/detail/cancer"]
#links =['https://en.wikipedia.org/wiki/Deep_learning']

count =1
for link in links:
    linklist=getLinks(link)
    print(linklist,"\n")
    with open("links.txt", "a") as f:
            for index,value in enumerate(linklist):
                f.write(value+"\n")

    print("URL Completed", count)
    count += 1
# for index,value in  enumerate(links):
#     print(value,"\n")



output = ''
blacklist = [
	# there may be more elements you don't want, such as "style", etc.
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script'
	'a',
	'p'

]


'''
count = 1
with open("links.txt","r") as hlinks:
	for url in hlinks:
		url = url.strip("/\n")
		res = requests.get(url)
		html_page = res.content
		soup = BeautifulSoup(html_page, 'html.parser')
		text = soup.find_all(text=True)

		for t in text:
			if t.parent.name not in blacklist:
	 			output += '{} '.format(t)

		print(output)

		with open("DeepLearning.txt","a") as file_write:
			file_write.write(output)

		print("URL:",count,"Completed")
		count = count +1
		
'''