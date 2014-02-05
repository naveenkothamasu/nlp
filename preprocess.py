#!usr/bin/env python
import glob
import re
import math
import sys

def getCategoryList():
	pFileName = ""
	files = glob.glob('*.[0-9]*.txt');
	for name in files:
		for c in re.findall('[^A-Z]', name):
                	name = name.replace(c,'')
	        if name != pFileName :
        	        numcategorylinesMap[name] = '0.0'
	        else:
        	        pFileName = name

def getCleanWordsCategory():

	numlines = 0.0
	lines = ""
	words = []
	f_out = open('spam_training.txt', 'w') #to make sure to delete one, if it exists
	f_out.close()
	f_out = open('spam_training.txt', 'a')

	for category in numcategorylinesMap:
		files = sorted(glob.glob(category + ".*.txt"));
		for path in files:
			f_in = open(path, "r")
			f_out.write(category+" ")
			for line in f_in:
				line = line.lower()	
				line = line.replace('<br />', ' ')
				
				specialchars = re.findall('[^a-z0-9]', line)	
				for s in specialchars:
					line = line.replace(s, ' ')
				
				extraspaces = re.findall('\s\s+', line);
				for s in extraspaces:
					line = line.replace(s,' ')
					
				f_out.write(line + " ")
			f_in.close()	
			f_out.write("\n");
	f_out.close()
####################### MAIN starts here #####################

numalllines = 0.0
#<category-name, num of lines>
numcategorylinesMap = {}

getCategoryList()
getCleanWordsCategory()
print("Generated spam_training.txt.")
######################## MAIN ends here ##############

