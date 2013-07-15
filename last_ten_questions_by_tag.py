#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

#10 viimeisintä kysymystä tietyllä tagilla

def haeKysymykset(termi):
	url = "http://api.avoindata.net/tags/title/"
	req = requests.get(url+termi)
	if req.status_code == 200:
		data = req.json()[termi]
		for row in data:
			print "%s\t%s" % (row['title'], row['view_count'])


if __name__ == '__main__':
	haeKysymykset("Tampere")