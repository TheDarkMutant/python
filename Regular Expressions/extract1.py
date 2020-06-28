# Extracting only the mail id from the line
# importing regular expressions library
import re

# file open
fhand = open('mbox-short.txt')

# \S+ at least one non blank before and after @
# Greedy
# ( ) to give you what you're looking for
# \S --> non-blank character
line = 'From stephen@u.nus.edu do not'
a = re.findall('^From (\S+@\S+)', line)
print(a)
