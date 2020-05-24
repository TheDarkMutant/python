try:
	h = raw_input("please input your hour:")
	hour = float(h)
	r = raw_input("please input your rate:")
	rate = float(r)
	if hour < 0:
		print("Please enter a valid number")
	elif rate < 0:
		print("Please enter a valid number")
	elif hour > 40:
		print("%.2f" % (40*rate+(hour-40)*1.5*rate))
	else:
		print("%.2f" % (hour*rate))
except:
		print("Please enter a valid number")
