# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
day = 365 * (90 - age)
week = 52 * (90 - age)
month = 12 * (90 - age)

print(f"You have {day} days, {week} weeks, and {month} months left.")