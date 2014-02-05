#!/usr/bin/env python
import sys
import math
from decimal import *

testfilename = sys.argv[2]
testfile = open(testfilename, "r")
modelfilename = sys.argv[1]
modelfile = open(modelfilename, "r")
modelfileDict = {}
wordlist = []
categoryList = []
numwordcategory = []
numcategorylines = []
linenum = 1;
numvocab = 0.0
numalllines = 0.0

for line in modelfile:
	
	templist= []
	wordlist = line.split()
	if(linenum == 1):
		numvocab = Decimal(wordlist[1].strip())
	elif(linenum == 2):
		numalllines = Decimal(wordlist[1].strip())
	elif(linenum == 3):
		categoryList.append(wordlist[1].strip())	
		categoryList.append(wordlist[2].strip())	
	elif(linenum == 4):
		numwordcategory.append(Decimal(wordlist[1].strip()))
		numwordcategory.append(Decimal(wordlist[2].strip()))	
	elif(linenum == 5):
		numcategorylines.append(Decimal(wordlist[1].strip()))
		numcategorylines.append(Decimal(wordlist[2].strip()))	
	else:
		templist.append(wordlist[1])
		templist.append(wordlist[2])
		modelfileDict[wordlist[0].strip()] = templist 
	linenum = linenum + 1;
modelfile.close()

currentProb = 0.0

for line in testfile:
	maxProb = -sys.maxint
	wordlist = line.split();
	i = 0;
	#resultsfile.write(wordlist[0].strip());
	for category in categoryList:
		firstTime = 1;
		currentProb = Decimal(math.log(numcategorylines[i]/numalllines))
		for word in wordlist:
			word = word.strip();	
			if firstTime == 1:
				firstTime = 0;
				continue;
			if word != "":
				if word in modelfileDict:
					currentProb += Decimal(modelfileDict[word][i])
				else:#word not present case
					currentProb += Decimal(math.log(Decimal(1.00)/(numwordcategory[i]+numvocab)))
		i = i+1;
		if(maxProb < currentProb):
			maxProb = currentProb;
			predicted = category
	print(predicted)
testfile.close()
