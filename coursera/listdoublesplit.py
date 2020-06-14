# Illustraion of double split of list
fname = input("Enter file name: ") # User Input
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname) # file open
count = 0
l = [i.split() for i in fh.readlines()
            if i.startswith("From") and i.find("@")>0 and len(i.split())>2] # split condition
for i in l:
    print(i[1]) 
    count+=1
print("There were", count, "lines in the file with *From* as the first word")
