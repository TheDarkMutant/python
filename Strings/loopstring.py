name = 'sanjiv'
index = 0
# looping through strings - Indeterminate loop [while]
print('indeterminate loop:')
while index < len(name):
    letter = name[index]
    print(index, letter)
    index += 1
# looping through strings - Determinate loop [for]
print('determinate loop:')
for i in name:
    print(i)
