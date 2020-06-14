# To arrange the words in a file alphabetically
fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'
fh = open(fname)
lst = list()
# Iterates through each line of the file
for line in fh:
    # Iterates through each word in line
    for i in line.split():
        # Checks for the word repitition in file
        if not i in lst:
            # Appends words to list
            lst.append(i)
# sorting the words
lst.sort()
print(lst) # Print the ordered list
