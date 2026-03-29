name = input("Write your name: ")
byear = int(input("Your birth year: "))
age = 2026 - byear
print(f"You are {age} years old")
print(f"Hello, {name}!")

if 1981 <= byear <= 1996:
    print("You're Millennial")
elif 1997 <= byear <= 2012:
    print("You're Gen Z")
else:
    print("Generation not determined")