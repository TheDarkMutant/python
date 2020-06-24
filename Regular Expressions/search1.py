# importing regular expression library
import re

# opening the file
fhand = open('mbox-short.txt')

# 1. search()
for line in fhand:
    line = line.rstrip()
    # Find 'From:' at the beginning of line
    # ^: beginning of
    # True/false if you find or not
    if re.search('^From:', line):
        print(line)
