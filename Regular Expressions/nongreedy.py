# importing regular expressions library
import re
# opening file
fhand = open('mbox-short.txt')
# Non-greedy matching to the nearest :
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
