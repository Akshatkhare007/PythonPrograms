
# program for making simple calculator

print("My Calculator")
print("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
a=float(input("Enter the first number ="))
b=float(input("Enter the second number ="))
z=int(input("Enter your choice ="))
match z:
 case 1:
  c=a+b
  print("Addition of numbers is =",c)
 case 2:
  c=a-b
  print("Subtraction of numbers is =",c)
 case 3:
  c=a*b
  print("Multiplication of numbers is =",c)
 case 4:
  c=a/b
  print("Division of numbers is =",c)
 case _:
  print("Invalid choice")
  



  









