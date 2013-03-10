#!/usr/bin/python
#

import datetime
import json
from pyquery import PyQuery as pq

companies = {
	'large-cap': {},
	'mid-cap': {},
	'small-cap': {},
}

for cap in companies:
	d = pq('http://www.di.se/borssidor/{0}/'.format(cap))

	for elem in d('#fh-stockLists-container tr'):
		if elem is not None and len( elem ):
			tdF  = pq('td:first-child', elem)

			link = pq(tdF.find('a')).attr('href')
			name = pq(tdF.find('a')).text()

			if link and 'stockwatch' in link:
				companies[cap][name.encode('utf8')] = link
				# print name, link
			

print json.dumps( companies, sort_keys=True, indent=4, separators=(',', ': ') )

#		splitD  = map(int, tdL.text().split('-'))


