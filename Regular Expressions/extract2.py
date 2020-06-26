import re

fhand = open('mbox-short.txt')

# Extracting only the domain
line = 'From stephen@u.nus.edu do not'
# find @ in line
# ( ) gives you what you're looking for
# [^ ] non blank
# * 0 or more
b = re.findall('@([^ ]*)', line)
print(b)
