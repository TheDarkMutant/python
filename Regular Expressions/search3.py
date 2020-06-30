# importing regular expressions library
import re

fhand = open('mbox-short.txt')

# 1. search()
for line in fhand:
    line = line.rstrip()
    # \S --> non-blank character
    # + --> one or more times
    # This basically searches for X- with non-blank characters up to :
    if re.search('^X-\S+:', line):
        print(line)
