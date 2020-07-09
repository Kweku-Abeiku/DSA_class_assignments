#this program checks if a number is negative, positive or zero.
print("This program checks if a number is negative, positive or zero.")
print("--------------------------------------------------------------")
number = float(input("Enter a number: "))
if number > 0:
   print(number,"is a positive number")
elif number == 0:
   print("This number is zero")
else:
   print(number,"is a negative number")