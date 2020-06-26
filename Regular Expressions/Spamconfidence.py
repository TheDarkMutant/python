# Extracting the highest value of spam confidence from a file
import re

fhand = open('mbox-short.txt')

# SPAM CONFIDENCE Example
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # skip those you don't find
    print(stuff)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximium:', max(numlist))
