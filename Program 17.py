
color = input("Enter the traffic light color Red, Yellow, Green: ")

match color.lower():
  case "red":
    print("Stop! The light is red.")
  case "yellow":
    print("Slow down! The light is yellow.")
  case "green":
    print("Go! The light is green.")
  case _:
    print("Invalid color Please select Red, yellow, or green.")