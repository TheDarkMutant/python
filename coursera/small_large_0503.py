# Determining the smallest and largest number entered
largest = None
smallest = None
# Indeterminate condition
while True:
    inp = input("Enter a number: ") # user input
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num
# Printing the smallest and largest numbers
print ("Maximum is", int(largest))
print ("Minimum is", int(smallest))
