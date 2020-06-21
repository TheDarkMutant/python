# Working with Strings in python
greet = ' Hello Sanjiv '

# To convert the string into lowercase letters
zap = greet.lower()
print(zap)

# To convert the string into uppercase letters
large = greet.upper()
print(large)

# To print the datatype set or used
what_type = type(greet)
print(what_type)

# To find a particular substring in the string.
what_dir = greet.find('lo')
print(what_dir)


replace_name = greet.replace('Sanjiv', 'MC')
print(replace_name)
# Replaces only the specific substring and not the value 

replace_letter = greet.replace('o', 'X')
print(replace_letter)
# To replace a particular letter in the string

strip_left = greet.lstrip() 
# Strips the trailing characters
strip_right = greet.rstrip()
# Strips the leading characters
strip_all = greet.strip()
# Strips both leading and trailing characters

print(strip_all)
print(strip_left)
print(strip_right)

start_with = greet.startswith('Hello')
print(start_with)
