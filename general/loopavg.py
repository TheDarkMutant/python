count = 0
sum = 0
print('Before', count, sum)
for i in [9,41,12,3,74,15]:
    count = count + 1
    sum += i
    print(count, sum, i)
print('After-\n')
print(count , sum , sum/count)
