#Kavilan Naidoo
#25-11-2014
#diamond

def input_odd_number():
    odd_number = int(input("Please enter an odd number: "))
    return odd_number

def bottom_half(odd_number):
    counter = odd_number - 2
    if odd_number % 2 == 1:
        while counter >0:
            list_1 = ""
            for count in range(counter):
                list_1 = list_1 + "*"
            counter = counter - 2
            print("{0:^{1}}".format(list_1,odd_number))

def top_half(odd_number):
    counter = 1
    if odd_number % 2 == 1:
        while counter <= odd_number:
            list_1 = ""
            for count in range(counter):
                list_1 = list_1 + "*"
            counter = counter + 2
            print("{0:^{1}}".format(list_1,odd_number))

def display_output(odd_number):
    top_half(odd_number)
    bottom_half(odd_number)

def two_pyramid():
    odd_number = input_odd_number()
    display_output(odd_number)

two_pyramid()
            
