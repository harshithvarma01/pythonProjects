input_range = int(input("Enter a number upto which number u want: "))
for number in range(1,input_range):
    if number % 3 ==0:
        print("Fizz")
        if number % 5 ==0:
            print("Fizz Buzz")
    elif number % 5 ==0:
        print("Buzz")
        if number % 3 ==0:
            print("Fizz Buzz")
    else:
        print(number)
