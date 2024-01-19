#While Loops:
#With the while loop we can execute a set of statements as long as a condition is true.

#Example:
i = 1
#While lopp repeats until a condition is false
while i < 6:
  print(i)
  if i == 50:
    break
i = i + 1

#Break:
#With the break statement we can stop the loop even if the while condition is true:

#Example:i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1