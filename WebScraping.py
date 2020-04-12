import requests
from bs4 import BeautifulSoup


output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script',
    'a'
    'p'
	# there may be more elements you don't want, such as "style", etc.
]

count = 1
with open("Total_Links.txt","r") as hlinks:
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

		with open("Cancer_Data.txt","a") as file_write:
			file_write.write(output)

		print("URL:",count,"Completed")
		count = count +1

