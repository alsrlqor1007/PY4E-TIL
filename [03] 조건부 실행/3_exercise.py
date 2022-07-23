hours = float(input('Hours: '))
ratePerHour = float(input('Rate per hour: '))

if hours > 40:
    overHours = hours - 40
    pay = (40 + (overHours * 1.5)) * ratePerHour
    print('Earned', pay)
else:
    pay = hours * ratePerHour
    print('Earned', pay)



# Lecture reference
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if fh > 40 :
	#print("Overtime")
	reg = fr * fh
	otp = (fh - 40.0) * (fr * 0.5)
	#print(reg, otp)
	xp = reg + otp
else:
	#print("regular")
	xp = fh * fr
print("Pay:", xp)