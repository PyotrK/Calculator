user_input = input()
from math import sqrt as square
print()
print()
print('Type "add" for addition')
print('Type "subtract" for subtraction')
print('Type "multiply" for multiplication')
print('Type "divide" for division')
print('Type "exit"to exit')
print('Type "commands" to view the commands')
while(user_input != "exit"):
 try:
  user_input = input("command:")
  if user_input == ("exit"):
   print("Exited")
  elif user_input ==(""):
   print("Please type a command")
  elif user_input == "commands":
   print('Type "add" for addition')
   print('Type "subtract" for subtraction')
   print('Type "multiply" for multiplication')
   print('Type "divide" for division')
   print('Type "exit"to exit')
   print('Type "commands" to view the commands')
  elif user_input == "add":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter number to add:"))
   print(num1+num2)
  elif user_input == "subtract":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 - num2)
  elif user_input == "divide":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 / num2)
  elif user_input == "multiply":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter a number to multiply:"))
   print(num1 * num2)
  elif user_input == "square root":
   num1 = float(input("Enter a number")
   print(square(num1))
  else:
   print('"' + user_input + '"' + " is not a command")
 except ZeroDivisionError:
  print(num1)
 except ValueError:
  print("Please enter a number")
 except:
  print("An unknown error ocurred.")
