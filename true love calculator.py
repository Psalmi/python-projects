# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
name = name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
total_1 = t + r + u + e
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
total_2 = l + o + v + e

love_total = str(total_1) + str(total_2)
love_score = int(love_total)


if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")