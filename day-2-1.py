# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

firstword = two_digit_number[0]
secondword = two_digit_number[1]
print(type(firstword))
result = int(firstword) + int(secondword)
print(result)
print(type(result))