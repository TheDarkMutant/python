# To compute Grade
# try block
try:
    s = raw_input("Enter your score:") # user input
    score = float(s) # Type conversion
# Conditional statement
    if score > 1.0: 
        print("Enter valid input")
    elif 1.0 >= score>=0.9:
        print("A")
    elif 0.9 > score>=0.8:
        print("B")
    elif 0.8 >score>=0.7:
        print("C")
    elif 0.7 >score>=0.6:
        print("D")
except:
    print("Invalid input, enter a valid input") # error message
