import sys

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

outputfile = open("output.txt", "w");
outputfile.close()


outputfile = open("output.txt", "a");

for line in inputfile:
	wordlist = line.split("\t")
	outputfile.write(wordlist[0].strip()+"\n")

outputfile.close()	
