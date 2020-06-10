# To determine average of numbers
total = 0
count = 0
while True: #indeterminate loop
    # user input
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
# computing average
average = total / count
print('Average: ', average) # display results

