#Kavilan Naidoo
#25-11-2014
#output symbols


def input_integer():
    integer = int(input("Please enter a number of times you would like the symbol displayed: "))
    return integer

def input_character():
    character = input("Please enter a symbol you would like to be dislpayed: ")
    return character

def program(integer, character):
    list_1 = ""
    for count in range(integer):
        list_1 = list_1 + character
    return list_1

def display_output(list_1):
    print(list_1)


def main_program():
    integer = input_integer()
    character = input_character()
    list_1 = program(integer,character)
    display_output(list_1)

main_program()




        
