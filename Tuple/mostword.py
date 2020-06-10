# To determine words used the most in a file
fhand = open('romeo.txt') # file open
counts = dict()
for line in fhand: # Iterate through every line of a file
    words = line.split()
    for word in words: # frequency of words
        counts[word] = counts.get(word,0) + 1 # 
lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v,k in lst[:10]:
    print(k,v)
