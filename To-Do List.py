def add():
    global x
    x = int(input("Where would you like to place new task? #Select a number 0-5"))
    myList.insert(x,"Up")
    run()

def view():
    print(myList)
    run()

def mark():
    option = int(input("Mark which task as done? "))
    run()

def remove():
    removal = int(input("Which task would you like to remove? 0 is first item on the list and last item is 5. "))
    myList.pop(removal)
    run()


myList = ["Indiana Jones", "Star Wars", "Ted", "Superman", "Superbad", "The Joker"]
print("Welcome to To-Do List!")
print("Please choose an operation ny entering a number 1-5")
print("1 = Add a task \n2 = View current to-do list \n3 = Mark task as completed \n4 = Remove a task from the to-do list \n5 = Quit")
option = int(input("Option: "))


def run():
    
    if option == 1: 
        add()

    if option == 2:
        view()

    if option == 3:
        mark()

    if option == 4:
        remove()
    
    if option == 5:
        quit()

run()

 