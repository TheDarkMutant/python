# importing regular expressions library
import re

fhand = open('mbox-short.txt')

# 1. search()
for line in fhand:
    line = line.rstrip()
    # * 0 or more digits, any number of times
    # . matches any character
    if re.search('^X.*:', line):
        print(line)
