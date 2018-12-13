#This file compares two .data files returned from getASN.py given as command line arguments
#It checks to see how many IP addresses are shared between the two files compared to how many ip addresses are in each file.

import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: python {} <file.data> <file2.data>\n".format(sys.argv[0]))
    sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

fileSet1 = {}
fileSet1 = set()

fileSet2 = {}
fileSet2 = set()

def openAndRead(filename,mySet):
    f = open(filename,"rb")
    for line in f:
        if "begin" not in line or "end" not in line:
            if line not in mySet:
                mySet.add(line)

openAndRead(file1,fileSet1)
openAndRead(file2,fileSet2)


differenceInSize = len(fileSet1) - len(fileSet2)
differenceSet = fileSet1 - fileSet2
lenDif = abs(len(differenceSet))
numTheSame = len(fileSet1) - lenDif


percentage = ((float(numTheSame) / len(fileSet2)) * 100) #if (len(fileSet1) > len(fileSet2)) else ((len(fileSet1) / len(differenceSet)) * 100)

print("Output:\n Size of %s: %d\n Size of %s: %d\n Difference in size of the files: %d\n IPs shared between the files: %d\n Percentage of %s shared with %s: %f\n" % (file1,len(fileSet1),file2,len(fileSet2),differenceInSize,numTheSame,file2,file1,percentage))


