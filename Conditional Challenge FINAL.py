#ricky
#10/18/2023
#Grade Conditionals


def grade(score):
    if (score >= 101):
        print("invalid")
    elif (score >= 90):
        print("A")
    elif (score >= 80):
        print("B")
    elif (score >= 70):
        print("C")
    elif (score >= 60): 
        print("D")
    elif (score <= -1):
        print("Invalid")
    else:
        print("F")

grade(101)