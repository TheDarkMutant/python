# importing regular expression library
import re
# opening file
fhand = open('mbox-short.txt')

line = 'From stephen@u.nus.edu do not'
# ^From --> starts From
# .* --> any character before @
# ( ) --> what you will get
# [^ ]* --> non-blank characters as many as them
c = re.findall('^From .*@([^ ]*)', line)
print(c)
