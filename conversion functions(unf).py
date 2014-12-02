#Kavilan Naidoo
#28-11-2014
#conversion rate

def input_conversion():
    print("You have the choice between pounds, euros and dollars")
    print("1.Pounds")
    print("2.Euros")
    print("3.Dollars")
    to_conversion = int(input("which would you like to convert to : "))
    from_conversion = int(input("which would you want to convert from: "))
    amount = float(input("Please enter the amount you want converted: "))
    return to_conversion, from_conversion, amount


def GBP_to_euro(amount):
    converted = amount * 1.229
    print("{0:.2f}".format(converted))

def GBP_to_dollar(amount):
    converted = amount * 1.601
    print("{0:.2f}".format(converted))

def euro_to_GBP(amount):
    converted = amount * 0.814
    print("{0:.2f}".format(converted))

def euro_to_dollar(amount):
    converted = amount * 1.302
    print("{0:.2f}".format(converted))

def dollar_to_GBP(amount):
    converted = amount * 0.625
    print("{0:.2f}".format(converted))

def dollar_to_euro(amount):
    converted = amount * 0.768
    print("{0:.2f}".format(converted))

def to_pounds(to_conversion, amount):
    if to_conversion == 3:
         GBP_to_dollar(amount)
    elif to_conversion == 2:
        GBP_to_euro(amount)
    
def to_euros(to_conversion, amount):
    if to_conversion == 3:
         euro_to_dollar(amount)
    elif to_conversion == 1:
        euro_to_GBP(amount)

def to_dollars(to_conversion, amount):
    if to_conversion == 2:
        dollar_to_euro(amount)
    elif to_conversion == 1:
        dollar_to_GBP(amount)

def from_convert(from_conversion, to_conversion, amount):
    if from_conversion == 1:
        to_pounds(to_conversion, amount)
    elif from_conversion == 2:
        to_euros(to_conversion, amount)
    else:
        to_dollars(to_conversion, amount)

def conversion():
    to_conversion, from_conversion, amount = input_conversion()
    from_convert(from_conversion, to_conversion, amount)






#main program
conversion()
        
        
    



    
    
        

