name1 = list(input("What is your name? "))
name2 = list(input("What is your crush's name?"))
com = name1 + name2
common_letters = []

# Iterate over a copy of name1 to avoid index errors
for char in name1[:]:
    if char in name2:
        name1.remove(char)
        name2.remove(char)
        common_letters.append(char)
lencom=len(common_letters)
lenname=len(com)
a=int(((2*lencom)/lenname)*100)
print("Your love percentage:",a)
