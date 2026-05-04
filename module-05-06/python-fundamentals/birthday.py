from datetime import datetime

bd = input("Your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(bd, "%Y-%m-%d")

today = datetime.now()

dow_born = birth_date.strftime("%A")
print(f"Day of week you were born: {dow_born}")

age = (today - birth_date).days
age_years = int(age / 365)
print(f"Your age: {age_years}")

next_birthday = birth_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"Days until next birthday: {days_left}")
