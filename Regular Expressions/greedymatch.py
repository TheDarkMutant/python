# Extraction using greedy matching technique where the search is expanded to maximum possible cases
# import regular expressions library
import re
# opening the file
fhand = open('mbox-short.txt')
# Greedy matching expanding out to the max :
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
