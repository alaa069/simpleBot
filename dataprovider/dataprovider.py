# Copyright (c) 2018 Alaa BEN JABALLAH

import wikipedia
import logging

class DataProvider(object):
	NOT_FOUND_MSG = "Sorry, I don't know this yet"

	def __init__(self):
		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

	def get_short_answer(self, query):

		try:
			# use wikipedia as failover
			wikiepedia_res = wikipedia.summary(query, sentences=1)
			logging.info("wikipedia res: {}".format(wikiepedia_res))
			if wikiepedia_res:
				return wikiepedia_res
		except:
			return self.NOT_FOUND_MSG
