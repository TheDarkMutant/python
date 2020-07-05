# importing regular expressions library
import re
# opening the file
fhand = open('mbox-short.txt')
# findall()
x = 'my 2 favourite numbers are 19 and 24'
# [0-9] digits and 1 or more digit
y = re.findall('[0-9]+', x)
print(y)
