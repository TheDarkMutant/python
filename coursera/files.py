# Accessing and manipulaating files
fname = input("Enter the file name: ") # user input
f = open(fname) # file open
for i in f:
    i = i.rstrip().upper()
    print(i)
