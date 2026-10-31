# WAP to input user's first name $ print its lengh.
name = input("enter the first name: ")
print(len(name))

#WAP to find the occurence of $ in a sting

str = "$ is american currency . 1$ = 100rp, I earing $ 5500$"
print(str.count("$"))

# WAP to check if a number entered by the user is odd or even.
number = int(input("enter the number:"))
if number %2 == 0:
    print("even")
else:
    print("old")


# WAP to find the greatest of 3 number entered by the user.
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>= b and a>= c:
    print("a is greater number")
elif b>= a and b >= c:
    print(" b is greater number")
else:
    print(" c is a greater number")


# WAP to check if a number is a multiple of 7 0r not.
num = int(input("enter the first number :"))
if num%7 == 0:
    print("num divible by 7")
else:
    print("num donot divible by 7")