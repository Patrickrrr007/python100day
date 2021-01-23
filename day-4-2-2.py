import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")

#Write your code below this line 👇

num_items = len(names)
#Generate random numbers between 0 and the last index. 
# -1是因為是從0開始
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

# 輸入 name, name
print(person_who_will_pay + " is going to buy the meal today!")






