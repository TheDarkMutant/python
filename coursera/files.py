fname = input("Enter the file name: ")
f = open(fname)
for i in f:
    i = i.rstrip().upper()
    print(i)
