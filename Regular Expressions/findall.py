# Extracting all numbers in a document
# importing regular expressions library
import re
# opening the file
fhand = open('mbox-short.txt')
# findall()
# extracting the numbers in the line
x = 'my 2 favourite numbers are 19 and 24'
# [0-9] digits and 1 or more digit
y = re.findall('[0-9]+', x)
print(y)
