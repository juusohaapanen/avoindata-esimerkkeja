import requests

url = "http://api.avoindata.net/tags"

r = requests.get(url)

tags = r.json()['tags']

for tag in tags:
	print "%s\t%s" % (tag['title'], tag['count'])