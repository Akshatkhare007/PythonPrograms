'''
code to enter age and check whether a person 
is minor, adult or a senior citizen
'''

a=int(input("Enter the age="))
if (a<18):
  print("You are a minor")
elif (a>=18 and a<65):
  print("You are an adult")
else:
  print("You are a senior citizen")




