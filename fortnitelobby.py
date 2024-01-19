#Warmup 11/7/23

#Initialize
import turtle
t = turtle.Turtle()
name = input("What is your name? ")
date = input("What is the date? ")
day = input("What day of the week is it? ")
age = int(input("How old are you? "))
coupon = input("Write your coupon code: ")

#This Function finds the price of the ticket based upon the information given
def price():
    global price
    if (age < 4):
        t.write(0)
        price = 0
    elif(age < 19) and (day == "Monday") or (day == "Tuesday") or (day == "Wednesday") or (day == "Thursday") or (day == "Friday") and (coupon != "Free Friday") and (coupon != "Sunday10"):
        t.write(15)
        price = 15
    elif(age < 19) and (coupon == "FreeFriday"):
        t.write(0)
        price = 0
    elif(age < 19) and (coupon == "Sunday10"):
        t.write(20)
        price = 20
    else:
        t.write(30)
        price = 30

#Functions

#Draws a text box with a label. This function uses a turtle to draw a text box with a label next to it.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box
def draw_textbox(label, y_location):
    t.penup()
    t.goto(-50, y_location)
    t.write(label, font=("Arial", 15, "bold"), align="right")
    t.pendown()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.goto(-40, y_location + 5)


#Draws a text box with a label. This function uses a turtle to draw a small text box with a label. The size of the text box is perfect for Y or N questions.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box  
def draw_small_textbox(label, y_location):
    t.goto(60, y_location)
    t.write(label, font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.goto(80, y_location + 5)


#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(string: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket  
def draw_ticket(name, price, Monday, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.penup()
    t.goto(50, y_location +75)
    t.write("Bus Ticket", font=("Arial", 15), align="right")
    t.goto(200, y_location +75)
    t.write(Monday, font=("Arial", 15), align="right")
    t.goto(100, y_location +35)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(100, y_location +5)
    t.write(price, font=("Arial", 15), align="right")


def ticketfinal():
    t.penup()
    t.goto(0,250)
    t.pendown()
    t.write("Fortnite Lobby" , align = "left" , font=("Arial", 15, "normal"))
    draw_textbox("Name:" , 200)
    t.write(name)
    draw_textbox("Day of the Week:" , 20)
    t.write(day)
    draw_textbox("Price:" , 150)
    price()
    draw_textbox("Coupon:" , 100)
    t.write(coupon)
    draw_ticket(name, price, day, -200)
    turtle.done()

#Main
ticketfinal()