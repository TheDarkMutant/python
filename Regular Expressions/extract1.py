import re

fhand = open('mbox-short.txt')

# \S+ at least one non blank before and after @
# Greedy
# ( ) gives you what you're looking for
# \S --> non-blank character
line = 'From stephen@u.nus.edu do not'
a = re.findall('^From (\S+@\S+)', line)
print(a)
