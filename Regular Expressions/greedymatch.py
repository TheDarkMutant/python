# import regular expressions library
import re
# opening file
fhand = open('mbox-short.txt')
# Greedy matching expanding out to the max :
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
