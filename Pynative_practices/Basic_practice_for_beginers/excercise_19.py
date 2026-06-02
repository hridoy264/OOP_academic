income = int(input("Enter your income: "))

if(income>=20000):
    tax = 10000*0.1 + (income-20000)*0.2 
elif(income>10000 and income<=20000):
    tax = income*0.1
else:
    tax = income*0

print("Tax:", tax)