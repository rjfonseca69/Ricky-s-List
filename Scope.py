#Scope 
#Initialize
#Global Variable
x=300
#Functions
def myfunc():
    #Local Variable
    global x
    x = x + 1
    print(x)
#Main

myfunc()