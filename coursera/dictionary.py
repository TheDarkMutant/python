name = input("Enter file:") # User Input
if len(name) < 1 : name = "mbox-short.txt"
f = open(name) # file open

dic = {}
maxvalue = 0
name = ""
l = [i.split()[1] for i in f.readlines()
            if i.startswith("From") and i.find("@")>0 and len(i.split()) > 2]
for i in l:
    if not dic.has_key(i):
        dic[i] = 1
    else:
        dic[i] +=1
        if maxvalue < dic[i]:
            maxvalue = dic[i]
            name = i
print(name,maxvalue)
