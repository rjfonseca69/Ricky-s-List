#ricardo fonseca
#Name:
#Date:

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws a text box with a label. This function uses a turtle to draw a text box with a label next to it.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box
t.penup()

def draw_textbox(label, y_location):
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
def draw_ticket(name, price, dayofweek, y_location):
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
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(200, y_location +75)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(100, y_location +35)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(100, y_location +5)
    t.write(price, font=("Arial", 15), align="right")
#Main
name = input("Whats your name?")
age = int(input("How old are you?"))
day = input("What day is it?")
coupon = input("Do you have a coupon code? Enter here")


draw_textbox("Name:", 100)
t.write(name, align="left", font=("Arial", 10,"normal"))
draw_textbox("Day of week:", 50)
t.write(day, align="left", font=("Arial", 10,"normal"))
draw_textbox("Age:", 0)
t.write(age, align="left", font=("Arial", 10,"normal"))
draw_textbox("Discount Code:", -50)
t.write(coupon, align="left", font=("Arial", 10,"normal"))
t.penup()
t.goto(-100,-100)
t.pendown()
t.write("1/1", align="left", font=("Arial", 10,"normal"))
t.write("13", align="left", font=("Arial", 10,"normal"))
draw_ticket("Fortnite Lobby", 30,"Friday",-150) 
turtle.done()
