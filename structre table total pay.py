#Kavilan Naidoo
#14-11-2014
#structre table total pay

basic_rate = float(input("Please enter your basic rate: "))
basic_hours = float(input("Please enter your basic hours: "))
overtime = float(input("Please enter your overtime hourse: "))
hours = basic_hours + overtime
pay = hours * basic_rate
pay = round(pay,2)
print("You are owed £{0}".format(pay,))


