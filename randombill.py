import random
names = input("Enter your names separated by comma")
nameslist = names.split(",")
length = len(nameslist)
random_choice = random.randint(0,length-1)
print(f"{nameslist[random_choice]} will pay the bill")