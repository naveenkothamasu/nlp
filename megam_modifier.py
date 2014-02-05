import sys

inputfilename = sys.argv[1];
outputfilename = sys.argv[2];

inputfile = open(inputfilename, "r");
outputfile = open(outputfilename, "r");

resultsfile = open("results.megam.txt", "w");
resultsfile.close()

resultsfile = open("results.megam.txt", "a");

for line in inputfile:
	wordlist = line.split(" ")
	word = wordlist[0].strip()
	line = outputfile.readline();
	wordlist = line.split(" ")
	word += " " + wordlist[0].strip();
	resultsfile.write(word+"\n")

inputfile.close()
outputfile.close()
resultsfile.close()
print 'generated results.megam.txt'
