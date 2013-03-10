#!/usr/bin/python
#

import datetime
import json
from pyquery import PyQuery as pq

filter = ['H&M B']

compaines = None
with open('stocklist.json', 'r') as f:
	companies = json.loads( f.read() )

for cap in companies:
	for comp in companies[cap]:
		if comp not in filter:
			continue

		stock_link = companies[cap][comp]

		d = pq(url='http://www.di.se{0}'.format(stock_link))

		for elem in d('#analysis-list-wrap tr'):
			if elem is not None and len( elem ):
				tdF     = pq('td:first-child', elem)
				tdS     = pq('td:nth-child(2)', elem)
				tdL     = pq('td:last-child',  elem)

				classes   = pq(tdF.find('a')).attr('class').split(' ')
				message   = pq(tdF.find('a')).text()
				announcer = pq(tdS.find('a')).text()
				splitD    = map(int, tdL.text().split('-'))
				date      = datetime.date(splitD[0], splitD[1], splitD[2])

				print date, announcer, 

				if 'diff-positive' in classes:
					print 'positive'
				elif 'diff-negative' in classes:
					print 'negative'
				elif 'diff-default' in classes:
					print 'default'


