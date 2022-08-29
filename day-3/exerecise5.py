# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
names = name1_lower + name2_lower
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true_count = (t + r + u + e)

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love_count = (l + o + v + e)
true_love_count = int(str(true_count) + str(love_count))

if (true_love_count < 10) or (true_love_count > 90):
  print(f"Your score is {true_love_count}, you go together like coke and mentos.")
elif (true_love_count >= 40) and (true_love_count <= 50):
  print(f"Your score is {true_love_count}, you are alright together.")
else:
  print(f"Your score is {true_love_count}.")

        

