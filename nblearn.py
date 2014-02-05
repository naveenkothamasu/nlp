#!/usr//bin/env python

import glob
import re
import math
import sys
from decimal import *

wordcategoryMap = {}
numvocab = 0.0
numalllines = 0.0
numcategorylinesMap = {}
numcategorywordMap = {}

def getConditionalProbWord(word, category):

	if word in wordcategoryMap[category]:
		count = Decimal(wordcategoryMap[category].get(word))+1;
	else:
		count = 1;
	'''	
	print('wod = %s' % word);	
	print ('count = %f' % count)
	print ('allwordcount in '+ category+' = %f' % numcategorywordMap[category])
	print('numvocab in ' + category + ' = %f' % numvocab)
	print ('lines in '+ category+' = %f' % numcategorylinesMap[category])
	print ('numalllines = %f' % numalllines)
	print numcategorywordMap;
	'''	
	return math.log(count) - math.log(numcategorywordMap[category]+numvocab);

####################### MAIN starts here #####################
trainingfilename = sys.argv[1] 
modelfilename = sys.argv[2] 

trainingfile = open(trainingfilename, 'r')
for line in trainingfile:
	numalllines += 1
	wordlist = line.split(" ")
	category = wordlist[0].strip();
	if category in numcategorylinesMap:
		numcategorylinesMap[category] += 1 
	else:
		numcategorylinesMap[category] = 1.0
		numcategorywordMap[category] = 1.0
		wordcategoryMap[category] = {} 
	del wordlist[0]
	for word in wordlist:
		word = word.strip()
		if word != "":
			numcategorywordMap[category] += 1;
			if word in wordcategoryMap[category]:
				wordcategoryMap[category][word] += 1;
			else:
				wordcategoryMap[category][word] = 0;
				numvocab += 1;
trainingfile.close()

modelfile = open(modelfilename, 'w')
modelfile.close()
modelfile = open(modelfilename, 'a')
modelfile.write('numvocab\t%f' % numvocab)
modelfile.write('\nnumalllines\t%f' % numalllines)

'''
Line 1: numvocab	<number>								
Line 2: numalllines	<number>
Line 3:	TOKEN	  	<class1>	<class2>	<class3>...	
Line 4:	wordcount	<number>	<number>	<number>					
Line 5:	linecount	<number>	<number>	<number>
Line 6: <token1>	<probability>	<probability>	<probability>
.
.
.
.					
'''

modelfile.write('\nTOKEN\t')
for category in numcategorylinesMap:
	modelfile.write(category+'\t\t')
modelfile.write('\nwordcount\t');
for category in numcategorylinesMap:
	modelfile.write('%f\t\t' % numcategorywordMap[category])
modelfile.write('\nlinecount\t');
for category in numcategorylinesMap:
	modelfile.write('%f\t\t' % numcategorylinesMap[category])

for category in numcategorylinesMap:
	for word in wordcategoryMap[category]:
		modelfile.write('\n' + word + '\t')
		for category in numcategorylinesMap:
			modelfile.write('%f\t' % getConditionalProbWord(word, category)),
######################## MAIN ends here ##############
