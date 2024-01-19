#Simple Calculator
#Ricardo Fonseca 
#11/29

#Init
#Functions
#Takes both parameters, adds them both together, and prints the result
def addition(number1, number2):
    solution = number1 + number2
    return(solution)
    run()

def subtraction(number1, number2):
    solution = number1 - number2
    return(solution)
    run()

def multiplication(number1, number2):
    solution = number1 * number2
    return(solution)
    run()

def division(number1, number2):
    solution = number1 / number2
    return(solution)
    run()

def modulus(number1, number2):
    solution = number1 % number2
    return(solution)
    run()


    


#Main
print("Welcome to Simple Calculator! Sponsored by Texas Instruments c. 2023")
print("Please choose an operation ny entering a number 1-5")
print("1 = addition \n2= subtraction \n3 = Multiplication \n4 = Division \n5 = Modulus \n6 = Quit the Program")
option = int(input("Option: "))


#Collect two numbers from the user to operate on ..
number1 = float(input("what is the first number: "))
number2 = float(input("What is the second number: "))

def run():
    
    if option == 1: 
        addition(number1, number2)

    if option == 2:
        subtraction(number1, number2)

    if option == 3:
        multiplication(number1, number2)

    if option == 4:
        division(number1, number2)

    if option == 5:
        modulus(number1, number2)

    if option == 6:
        quit()

print 
