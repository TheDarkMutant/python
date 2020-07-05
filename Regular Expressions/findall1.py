# importing regular expressions library
import re
# opening the file
fhand = open('mbox-short.txt')
# findall()
x = 'my 2 favourite numbers are 19 and 24'
# Find all one or more vowels
y = re.findall('[AEIOU]+', x)
print(y)
