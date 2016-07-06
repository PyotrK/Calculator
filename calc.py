mem_input = input
user_input = input
m = 0
lastnum = 0
from math import sqrt
print()
print()
print('Mathematical commands:')
print('Type "add" for addition')
print('Type "subtract" for subtraction')
print('Type "multiply" for multiplication')
print('Type "divide" for division')
print('Type "modulo" for modulo division')
print('Type "floor" for floor division')
print('Type "square" for square root')
print('Type "exponent" for exponentation')
print()
print('Memory commands:')
print('Type "m" to edit the number in memory with a matematical comand')
print('Type "mv" to view the number in memory')
print('Type "m+" to add the last number to memory')
print('Type "m-" to subtract the last number from memory')
print()
print('Other commands:')
print('Type "num" to add a number to the last number')
print('Type "last" to show the last number')
print('Type "exit"to exit')
print('Type "commands" to view the commands')
print()
while(user_input != "exit"):
 try:
  user_input = input("command:") 
  if user_input == ("exit"):
   print("Exited")
  elif user_input == ("last"):
   print(lastnum)
  elif user_input == ("num"):
   num3 = float(input("Number:"))
   lastnum = num3
   print(num3)
  elif user_input ==(""):
   print("Please type a command")
  elif user_input == "commands": 
   print()
   print()
   print('Mathematical commands:')
   print('Type "add" for addition')
   print('Type "subtract" for subtraction')
   print('Type "multiply" for multiplication')
   print('Type "divide" for division')
   print('Type "modulo" for modulo division')
   print('Type "floor" for floor division')
   print('Type "square" for square root')
   print('Type "exponent" for exponentation')
   print()
   print('Memory commands:')
   print('Type "m" to edit the number in memory with a matematical comand')
   print('Type "mv" to view the number in memory')
   print('Type "m+" to add the last number to memory')
   print('Type "m-" to subtract the last number from memory')
   print()
   print('Other commands')
   print('Type "num" to add a number to the last number')
   print('Type "last" to show the last number')
   print('Type "exit"to exit')
   print('Type "commands" to view the commands')
   print()
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
   lastnum = num1 ** num2
  elif user_input == "m":
   mem_input = input("Mathematical command:")
   if mem_input == "add":
    num = float(input("Enter a number:"))
    print(str(m)+' '+'+'+' '+str(num))
    print("= "+str(m + num))
    m = m + num
   elif mem_input == "subtract":
    num = float(input("Enter a number:"))
    print(str(m)+' '+'-'+' '+str(num))
    print("= "+str(m - num))
    m = m - num
   elif mem_input == "divide":
    num = float(input("Enter a number:"))
    print("= "+str(m / num))
    m = m / num
   elif mem_input == "multiply":
    num = float(input("Enter a number:"))
    print("= "+str(m * num))
    m = m * num
   elif mem_input == ("square"):
    print(sqrt(m))
    m = sqrt(m)
   elif mem_input == ("modulo"):
    num = float(input("Enter a number:"))
    print(m % num)
    m = m % num
   elif mem_input == ("floor"):
    num = float(input("Enter a number:"))
    print(m // num)
    m = m // num
   elif mem_input == ("exponent"):
    num = float(input("Enter a number:"))
    print(m ** num)
    m = m ** num
   else:
    print('"' + str(mem_input) + '"' + " is not a mathematical command")
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
