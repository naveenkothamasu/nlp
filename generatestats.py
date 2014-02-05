#!/usr/bin/env python
import sys
from decimal import *

actualsfilename = sys.argv[1]
resultsfilename = sys.argv[2]

correctly_classified_as_c = 0.0
classified_as_c =0.0
belongs_in_c = 0.0
categoryMap = {}
precisioncategoryMap = {}
recallcategoryMap = {}
f_scorecategoryMap = {} 
precision = 0.0
recall = 0.0

resultsfile = open(resultsfilename, "r")
actualsfile = open(actualsfilename, "r")

for line in actualsfile:
	wordlist = line.split()
	if wordlist[0] not in categoryMap:
		categoryMap[wordlist[0].strip()] = 0.0
actualsfile.close()
print categoryMap
num = 0.0
den =0.0
for category in categoryMap:
	correctly_classified_as_c = 0.0
	classified_as_c =0.0
	belongs_in_c = 0.0
	
	resultsfile = open(resultsfilename, "r")
	actualsfile = open(actualsfilename, "r")
	for line in resultsfile:
		#wordlist = line.split("\t") #TODO
		wordlist = line.split() #TODO
		predicted = wordlist[0].strip()
		predicted = predicted.replace('\n','')
		actual = actualsfile.readline().strip();
		if category == actual: 
			belongs_in_c += 1
			if actual == predicted:
				correctly_classified_as_c += 1	
				classified_as_c +=1
		elif category == predicted:
			classified_as_c +=1
			den +=1;

	print '\n'+category
	print '------'
	print 'correctely_classified_as_c %f' % correctly_classified_as_c
	print 'classified_as_c %f' % classified_as_c
	print 'belongs_in_c %f' % belongs_in_c
	precision = Decimal(correctly_classified_as_c)/Decimal(classified_as_c)
	recall = Decimal(correctly_classified_as_c)/Decimal(belongs_in_c)
	print 'precision %0.3f' % precision
	print 'recall %0.3f' % recall 
	precisioncategoryMap[category] = precision
	recallcategoryMap[category] = recall
	f_scorecategoryMap[category] = (Decimal(2.0) * precision*recall)/(precision + recall)
	num =num+ correctly_classified_as_c
	print 'f-score %0.3f' % f_scorecategoryMap[category]
	resultsfile.close()
	actualsfile.close()
accuracy = (num)/(num+den)

print ('\nAccuracy %0.3f' % accuracy)

