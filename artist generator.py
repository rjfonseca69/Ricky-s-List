#Ricardo Fonseca
#10/24/2023
#Artist Generator 

print("Welcome to the Office Character Game!")
print("Answer the questions to find your character")
ans = input("male or female?")
if ans == "male":
    ans = input("funny or serious?")
    if ans == "funny":
        ans = input("manager or sales?")
        if ans == "manager":
            print("Your Office character is Michael Scott")
        else:
            print("Your Office character is Jim Halpert")
    if ans == "serious":
        ans = input("sales or HR?")
        if ans == "sales":
            print("Your Office character is Stanley Hudson")
        else:
            print("Your Office character is Toby Flenderson")
if ans == "female":
    ans = input("funny or serious?")
    if ans == "funny":
        ans = input("receptionist or HR?")
        if ans == "receptionist":
            print("Your Office character is Pam Beesly")
            if ans != "receptionist":
                print("Your Office character is Kelly Kapoor")
    if ans == "serious":
        ans = input("accounting or sales")
        if ans == "accounting":
            print("Your Office character is Phyllis Vance")
            if ans != "accounting":
                print("Your Office Character is Angela Martin")
