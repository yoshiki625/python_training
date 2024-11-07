# Control flow

# if ...else _ Decision meking

no_of_person = 2

if no_of_person <= 2:
    print("We will take the bike")
else:
    print("We will take the car")

# Task
# Get two person name
# Case 1:
# Luffy, Zoro
# 173cm, 163cm
# Expected
# Luffy is taller than Zoro by 10cm


# Case 2:
# Luffy, Zoro
# 173cm, 185cm
# Expected
# Zoro is taller than Luffy by 12cm

# sol1
name1 = input("Input name1 :")
name2 = input("Input name2 :")
name1_height = float(input("Input name1_height :"))
name2_height = float(input("Input name1_height :"))

if name1_height > name2_height:
    print(f"{name1} is taller than {name2} by {name1_height-name2_height}cm")
else:
    print(f"{name2} is taller than {name1} by {name2_height-name1_height}cm")


# sol2
captain_name = input("Please tell me the captain name?:")
vice_captain_name = input("Please tell me the vice captain name?:")
captain_height = float(input("Please tell me the captain name?:"))
vice_captain_height = float(input("Please tell me the vice captain name?:"))

diff_height = abs(captain_height - vice_captain_height)

if captain_height > vice_captain_height:
    print(f"{captain_name} is taller than {vice_captain_name} by {diff_height}cm")
else:
    print(f"{vice_captain_name} is taller than {captain_name} by {diff_height}cm")

# Task 1.2

# if same height
captain_name = input("Please tell me the captain name?:")
vice_captain_name = input("Please tell me the vice captain name?:")
captain_height = float(input("Please tell me the captain name?:"))
vice_captain_height = float(input("Please tell me the vice captain name?:"))

diff_height = abs(captain_height - vice_captain_height)

if captain_height > vice_captain_height:
    print(f"{captain_name} is taller than {vice_captain_name} by {diff_height}cm")
elif captain_height == vice_captain_height:
    print(f"{captain_name} and {vice_captain_name} are of same height")
else:
    print(f"{vice_captain_name} is taller than {captain_name} by {diff_height}cm")

# if and else _ only one
# elif _ many

# homework

fav_flavour = input("what's your fav flavour? ")

# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

# Case 1:
# Yes, we do have vanilla

# Case 2:
# "orange"
# Sorry, we ran out of orange

# sol1
if (
    fav_flavour == stock1
    or fav_flavour == stock2
    or fav_flavour == stock3
    or fav_flavour == stock4
):
    print(f"Yes, we do have {fav_flavour}")
# else stock == fav_flavour:
else:
    print(f"Sorry, we ran out of {fav_flavour}")


# sol2
fav_flavour = input("what's your fav flavour? ")

# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

if fav_flavour == stock1:
    print(f"Yes, we do have {stock1}")
elif fav_flavour == stock2:
    print(f"Yes, we do have {stock2}")
elif fav_flavour == stock3:
    print(f"Yes, we do have {stock3}")
elif fav_flavour == stock4:
    print(f"Yes, we do have {stock4}")
else:
    print(f"Sorry, we ran out of {fav_flavour}")


# sol3
fav_flavour = input("what's your fav flavour? ")

# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

if fav_flavour in (stock1, stock2, stock3, stock4):
    print(f"Yes, we do have {fav_flavour}")
else:
    print(f"Sorry, we ran out of {fav_flavour}")

# sol3
fav_flavour = input("what's your fav flavour? ").strip().lower()

# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

if not (fav_flavour in (stock1, stock2, stock3, stock4)):
    print(f"Sorry, we ran out of {fav_flavour}")
else:
    print(f"Yes, we do have {fav_flavour}")

# ctrl + , _ settings
