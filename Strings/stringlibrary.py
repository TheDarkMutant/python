# Working with Strings in python
greet = ' Hello Sanjiv '

zap = greet.lower()
print(zap)
# Converts the string to lowercase letters

large = greet.upper()
print(large)
# Converts the string to uppercase letters

what_type = type(greet)
print(what_type)
# To print datatype

what_dir = greet.find('lo')
print(what_dir)
# To find a particular substring in the string.

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
