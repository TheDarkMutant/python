# importing regular expression library
import re
# opening file
fhand = open('mbox-short.txt')

# Extracting only the domain of the id
line = 'From stephen@u.nus.edu do not'
# find @ in line
# ( ) to give you what you're looking for
# [^ ] non blank
# * 0 or more
b = re.findall('@([^ ]*)', line)
print(b)
