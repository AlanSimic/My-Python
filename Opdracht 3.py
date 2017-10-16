input("To stop the program, answer 'Do u want to add, subtract, multiply or divide?' with q"", to begin, press enter!")
a = float(input("Insert a number here : "))
m = input("Do u want to add, subtract, multiply or divide? : ")
if m == "q":
     quit(print("Program ended"))
b = float(input("Insert a second number here : "))

if m == 'add':
    result = a + b
if m == 'subtract':
    result = a - b
if m == 'multiply':
    result = a * b
if m == 'divide':
    result = a / b
print(result)


while m != True:
 p = (input("Do u want to add, subtract, multiply or divide? : "))

 if p == "q":
        quit(print("Program ended"))
        break

 y = float(input("Insert another number here : "))
 if p == "add":
    result = result + y
 if p == "subtract":
    result = result - y
 if p == "multiply":
    result = result * y
 if p == "divide":
    result = result / y






 print(result)
