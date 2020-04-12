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


url = "https://en.wikipedia.org/wiki/Osama_bin_Laden"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)




for t in text:
	if t.parent.name  not in blacklist:
	 	output += '{} '.format(t)

	print(output)