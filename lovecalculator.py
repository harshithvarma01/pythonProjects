name1 = input("What is your name? ")
name2 = input("What is your crush name?")
combinedname = name1 + name2
req_name = combinedname.lower()
t = req_name.count('t')
r = req_name.count('r')
u = req_name.count('u')
e = req_name.count('e')
true = t + r + u + e

l = req_name.count('l')
o = req_name.count('o')
v = req_name.count('v')
e = req_name.count('e')
love = l + o + v + e

lovescore = str(true) + str(love)
score = int(lovescore)
if score < 10 or score >90:
    print(f"your love score is {score} and you go together like coke and mentos")
elif score >=40 and score <= 50:
    print(f"your love score is {score} and you are alright together ")
else:
    print(f"your love score is {score}")