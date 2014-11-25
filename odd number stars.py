#Kavilan Naidoo
#25-11-2014
#odd number stars

def input_odd_number():
    odd_number = int(input("Please enter an odd number: "))
    return odd_number

def main_program(odd_number):
    counter = odd_number
    if odd_number % 2 == 1:
        while counter >0:
            list_1 = ""
            for count in range(counter):
                list_1 = list_1 + "*"
            counter = counter - 2
            print("{0:^{1}}".format(list_1,odd_number))
            
def display_ouput(odd_number):
    main_program(odd_number)

def pyramid():
    odd_number = input_odd_number()
    main_program(odd_number)
 

pyramid()
        
