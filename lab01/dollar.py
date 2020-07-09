#This program converts dollars to Ghana cedis.
print("This program converts dollars to Ghana cedis.")
print("----------------------------------------------")
dollars = float(input("Enter amount in dollars: "))

# dollar rate
rate = float(input("Enter current dollar rate: "))

cedis = dollars * rate
print('%0.2f dollars is equal to %0.2f cedis' %(dollars,cedis))