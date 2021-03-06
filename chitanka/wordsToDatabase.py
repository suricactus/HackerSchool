#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import time
import sys
import langid

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
conn = psycopg2.connect("host='' port='5432' dbname='chitanka' user='postgres' password=''")
cur = conn.cursor()

iterator = 0

try:
	with open('/home/slavi/Desktop/words.txt', 'r') as f:
		startMain = time.time()
		startInner = time.time()
		for line in f:
			iterator += 1
			if iterator%100000 == 0:
				timeTakenFor100000words = time.time() - startInner
				print "{} words iterated!".format(iterator)
				print "Time taken for 100k words: {} seconds".format(timeTakenFor100000words)
				startInner = time.time()
			try:
				word = line.split('\n')[0].decode('utf-8').lower()
				query = "INSERT INTO dictionary VALUES ('%s');"% (word)
				cur.execute(query)
			except:
				conn.rollback()
				pass
			else:
				conn.commit()
		timeTaken = time.time() - startMain
		print "Total time taken: {} seconds".format(timeTaken)
except IOError:
	print "Could not open file!"
	sys.exit()

cur.execute("SELECT count(*) FROM dictionary")
WordsInBGLanguage = cur.fetchone()
WordsInBGLanguage = WordsInBGLanguage[0]
print "According to my dictionary, WordsInBGLanguage are: {}".format(WordsInBGLanguage)
cur.close()
conn.close()