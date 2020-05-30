# To compute gross pay of electricity usage
try:
	h = raw_input("please input your hour:") # User input for hour
	hour = float(h) # Type conversion
	r = raw_input("please input your rate:") # User input for rate 
	rate = float(r)
	if hour < 0:
		print("Please enter a valid number") # error message
	elif rate < 0:
		print("Please enter a valid number") # error message
	elif hour > 40:
		print("%.2f" % (40*rate+(hour-40)*1.5*rate)) # Equation for Overtime usage
	else:
		print("%.2f" % (hour*rate)) # Equation for Normal usage
except:
		print("Please enter a valid number") # Error message
