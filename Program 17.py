'''
program to enter the colour of traffic light
and print the required information
'''
color = input("Enter the colour of traffic light- Red, Yellow or Green:")

match color.lower():
  case "red":
    print("Stop! The light is red.")
  case "yellow":
    print("Slow down! The light is yellow.")
  case "green":
    print("Go! The light is green.")
  case _:
    print("Invalid color. Please select Red, Yellow or Green.")
