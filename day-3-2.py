# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# # BMI = round(weight / height ** 2)
# # if BMI < 18.5:
# #   print(f'Your BMI is {BMI}, you are underweight')
# # elif BMI < 25:
# #   print(f'Your BMI is {BMI}, you are normal weight')
# # elif BMI < 30:
# #   print(f'Your BMI is {BMI}, you are slightly weight')
# # elif BMI < 35:
# #   print(f'Your BMI is {BMI}, you are obese')
# # else:
# #   print(f'Your BMI is {BMI}, you are clinically obese')

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
# 	print(f"Your bmi is {bmi}, you are underwight")
# elif bmi < 25:
# 	print(f"Your bmi is {bmi}, you are normal weight")
# elif bmi < 30:
# 	print(f"Your bmi is {bmi}, you are overwight")
# elif bmi < 35:
# 	print(f"Your bmi is {bmi}, you are underwight")
# else:
# 	print(f"Your bmi is {bmi}, you are clinically obese.")

ID = input()
year = int(ID[1:3]) #指整個字串的第 2、3
if year < 4:
    print("Graduated")
elif year <= 7 and year >= 4:
    if year == 7:
        print("Freshman")
    elif year == 6:
        print("Sophomore")
    elif year == 5:
        print("Junior")
    elif year == 4:
        print("Senior")
else:
    print("Not Registered Yet")