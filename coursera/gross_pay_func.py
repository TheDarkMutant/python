# Function to compute gross_pay
def computepay(h,r):
    if(h < 0 or r < 0):
        return 'Enter valid inputs'
    elif(h > 40):
        return(40*r+(h-40)*1.5*r)
    else:
        return(h*r)

# Taking inputs
hrs = input("Enter the number of hours")
h = float(hrs)
rate = input("Enter the rate")
r = float(rate)

# Invoking function for computation
p = computepay(h,r)

# Displaying the result
print("Pay",p)
