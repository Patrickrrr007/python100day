import random
print("\n")

# 1.random.random()
# 只有0~1的隨機小數
print("隨機數：", random.random(), "\n")

# 2.random.uniform()
# 不是random.randomuniform
# 指定數字的隨機小數
print(random.uniform(0, 2), "\n")

# 3.random.randint()
# 不是random.randomint()
# 指定數字的隨機 "整" 數
print(random.randint(10, 20), "\n")

# 4.random.randrange()
# 0 ~ 100 選出一個14的倍數
print(random.randrange(0, 100, 14), "\n")

# 5.random.choice
# randomly choice one
# 可以是字串或列表中的隨機一個
print (random.choice("www.jb51.net"), "\n")

# 6.random.shuffle()
# 打亂序列
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(x)
print(x, "\n")

# 7.random.sample()
# num 任意取 3
num = [10, 20, 30, 40, 50]
print(random.sample(num, 3), "\n")
	