user_input = input
m = 0
lastnum = 0
from math import sqrt
print()
print()
print('Type "add" for addition')
print('Type "subtract" for subtraction')
print('Type "multiply" for multiplication')
print('Type "divide" for division')
print('Type "modulo" for modulo division')
print('Type "floor" for floor division')
print('Type "square" for square root')
print('Type "exponent" for exponentation')
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
   print('Type "modulo" for modulo division')
   print('Type "floor" for floor division') 
   print('Type "square" for square root')
   print('Type "exponent" for exponentation')
   print('Type "exit"to exit')
   print('Type "commands" to view the commands')
  elif user_input == "add":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter number to add:"))
   print(num1+num2)
   lastnum = (num1 + num2)
  elif user_input == "subtract":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 - num2)
   lastnum = (num1 - num2)
  elif user_input == "divide":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 / num2)
   lastnum = (num1 / num2)
  elif user_input == "multiply":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter a number to multiply:"))
   print(num1 * num2)
   lastnum = (num1 * num2)
  elif user_input == "modulo":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 % num2)
   lastnum = (num1 % num2)
  elif user_input == "floor":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 // num2)
   lastnum = (num1 // num2)
  elif user_input == "square":
   x = float(input("Enter a number:"))
   print(sqrt(x))
   lastnum = sqrt(x)
  elif user_input == "exponent":
   num1 = float(input("Enter a number:"))
   num2 = float(input("Enter another number:"))
   print(num1 ** num2)
   lastnum (num1 ** num2)
  elif user_input == "m":
   print(m)
   
  elif user_input == "mv":
   print(m)
  elif user_input == "mc":
   m = 0
   print("memory cleared")
  elif user_input == "m+":
   print(str(m) + " = last memory")
   m = m + lastnum
   print(str(m) + " = new memory")
  elif user_input == "m-":
   print(str(m) + " = last memory")
   m = m - lastnum
   print(str(m) + " = last memory")
  elif user_input == "clear":
   count = 50
   while count != 0:
    print("")
    count -= 1
  else:
   print('"' + user_input + '"' + " is not a command")
 except ZeroDivisionError:
  print(num1)
 except ValueError:
  print("Please enter a number")
 except:
  print("An unknown error ocurred.")