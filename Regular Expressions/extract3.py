# importing regular expression library
import re
# opening the file
fhand = open('mbox-short.txt')
# applying alternate expression to extract the domain of the id
line = 'From stephen@u.nus.edu do not'
# ^From --> starts From
# .* --> any character before @
# ( ) --> what you will get
# [^ ]* --> non-blank characters as many as them
c = re.findall('^From .*@([^ ]*)', line)
print(c)
