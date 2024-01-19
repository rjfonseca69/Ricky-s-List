#Leap Year
#If a year is divisible by 4, it is a leap year.
#However, if that year is also divisible by 100, it is not a leap year, unless
#it is divisible by 400. In that case, it is a leap year.



def tracker():
    x = int(input("enter the year"))
    if (x % 4 == 0):
        return("True")
    if (x % 4 == 0) and (x % 100 == 0):
        return("False")
    if (x % 4 == 0) and (x % 100 == 0) and (x % 400 == 0):
        return("True")
    else:
        return("False")
print(tracker())