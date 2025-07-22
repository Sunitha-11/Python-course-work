#1.positive or negative
num=int(input("Enter the number:"))
if num>0:
     print("postive number")
else:
    print("negative number")



#2.even or odd
num=int(input("enter the number:"))
if num%2==0:
     print(f"{num} is even number")
else:
     print(f"{num} is odd number")



#3.divisible by 5
num=int(input("enter the number:"))
if num%5==0:
     print(f"{num} number is divisible by 5")
else:
     print(f"{num} number is not divisible by 5")


#4.divisible by 3 and 7
num=int(input("enter the number"))
if num%3 & num%7==0:
          print(f"{num} is divisible by both 3 and 7")
else:
     print(f"{num} is not divisible by both 3 and 7")

#5.leap year checking
year=int(input("enter the year:"))
if(year%4==0 and year%100!=0 ) or(year%400==0):
     print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")


#check pass or fail
#only this part of code will run
marks=int(input("enter the number:"))
if marks<35:
     print("you failed in test,better luck next time!!")
elif marks>=35:
     print("you passed the test,congrats!!")


#check 3 digit number
number=int(input("enter the number:"))
if number<1000:
     print(f"{number} is 3 digit number")
else:
     print(f"{number} is not a 3 digit number")


#checks vowel or not
ch=input("enter the character:")
if ch.lower() in ["a","e","i","o","u"]:
     print("it is vowel")
else:
     print("itsnot vowel")




#greatest number
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
     print("a is greater")
elif b>a:
     print("b is greater")
else:
     print("both are equal")


#smallest number
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
     print("a is smaller")
elif b>a:
     print("b is smaller")
else:
     print("both are equal")





#check if number=0
num=int(input("enter the number"))
if num==0:
     print("number is zero")
else:
     print("number is not zero")




#check num is multiple of 10
n=int(input("enter the number:"))
if n*10==0:
     print(f"{n} is multiple of 10")
else:
     print(f"{n} is not multiple of 10")


#vote eligible
age=int(input("Enter the age:"))
if age<18:
     print(f"{age} is not eligible to vote")
elif age>=18:
     print(f"{age} is eligible to vote")
else:
     print("enter the correct age")


#number is in between 1 and 100
num=int(input("enter the number:"))
if num>0 and num<101:
    print(f"{num} is in range between 1 and 100")
else:
    print(f"{num} is not in range between 1 and 100")



#check the square of all number
i=int(input("enter the number"))
for i in range(1,11):
    print(f"square of {i} is {i**2}")


#check the square of any number
i1=int(input("enter the number"))
i2=int(input("enter any number:"))
if i1==i2**2:
    print(f"{i1} is square of{i2}")
elif i2==i1**2:
    print(f"{i2} is square of {i1}")
else:
    print("both numbers are not square to each other")



string1=input("enter the name:")
string2=input("enter the name:")
if string1==string2:
    print(f"{string1} is equal to {string2}")
elif string1!=string2:
    print(f"{string1} is not equal to {string2}")



#check the number is prime
num=int(input("enter the number:"))
if num>1:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
        if is_prime:
            print("number is prime")
    else:
        print("not a prime number")
else:
    print("number is not prime")



#check positive and even
num=int(input("enter the number:"))
if num>0 and num%2==0:
    print(f"{num}the number is positive and even")
else:
    print(f"{num}the number is not  positive and even")



#check the uppercase or not
ch=input("enter the character:")
if ch.isupper():
    print(f"{ch} is in uppercase")
else:
    print(f"{ch} is noot in uppercase")



#check the temperature
temp=int(input("enter the number:"))
if temp> 35:
    print("temperature is hot")
else:
     print("temperature is cool")




#check if number is 4 digit even or not
num=int(input("enter the number:"))
if num>999 and num<=9999 and num%2==0:
 print(f"{num} is 4 digit and even")
else:
 print(f"{num} is not 4 digit and even")


#palindrome number
num=int(input("enter the number:"))
original=str(num)
reverse_num=original[::-1]
if original==reverse_num:
    print("palindrome number")
else:
    print("not a palindrome number")



#str long
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("First string is longer")
elif len(str1) < len(str2):
    print("Second string is longer")
else:
    print("Both strings are of equal length")


#square root
num = int(input("Enter a number: "))
root = int(num ** 0.5)

if root * root == num:
    print("Perfect square")
else:
    print("Not a perfect square")

#Check if an angle is acute, right, or obtuse
angle = int(input("Enter an angle in degrees: "))

if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")


num=int(input("enter the number:"))
original=str(num)
reverse_num=original[::-1]
if original==reverse_num:
    print("palindrome number")
else:
    print("not a palindrome number")
