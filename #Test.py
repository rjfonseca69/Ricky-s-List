#Test
#This question asks which if statements evaluate to True.
#Notice how in computer science, we do not need a boolean expression inside of ifs. As long as we have a boolean, the ifs will still work.
hot = True
humid = False

if hot:
    print(hot and humid)
if not(humid):
    print(hot or humid)
if hot or humid:
    print(hot)
if hot and humid:
    print(hot)

#Timer Questions
#This answer looks correct but it is not. The IF statements are overwriting eachother.
#This can be fixed by making it an if, else if, else if.
timer = 90
if timer > 60:
    bonus = 1500
if timer >= 30:
    bonus = 1000
if timer < 30:
    bonus = 500
print(bonus) 