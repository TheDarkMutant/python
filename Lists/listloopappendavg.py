# Computing average with inbuilt functions
numlist = list() 
while True:
    inp = input('Enter a number: ') # User inout
    if inp == 'done' :  break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)
