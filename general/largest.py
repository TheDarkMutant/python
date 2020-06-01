# To determine largest number in the list
largest = -1
print('Before', largest)
for i in [9,41,12,3,74,15]:
    if(i > largest):
        largest = i
    print(largest, i)
print("After", largest)
