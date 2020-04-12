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
	'a',
	'p'
]

url = "https://www.medicinenet.com/hiv/focus.htm"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)


for t in text:
	if t.parent.name  not in blacklist:
		output += '{} '.format(t)

	print(output)