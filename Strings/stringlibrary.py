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

# TOoreplace a specific substring and not value 
replace_name = greet.replace('Sanjiv', 'MC')
print(replace_name)

# To replace a particular letter in the string
replace_letter = greet.replace('o', 'X')
print(replace_letter)

# Strips the trailing characters
strip_left = greet.lstrip() 

# Strips the leading characters
strip_right = greet.rstrip()

# Strips both leading and trailing characters
strip_all = greet.strip()


print(strip_all)
print(strip_left)
print(strip_right)

start_with = greet.startswith('Hello')
print(start_with)
