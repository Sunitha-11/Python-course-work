#Print numbers from 1 to 20 using a for loop.
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(i,end=" ")         #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20



#2Print all elements of a given list.
cities = input("enter the string:")
for city in cities:
    for i in range(1,5):
       print(cities)



#Print all even numbers between 1 and 50
num=int(input("enter the number:"))
for i in range(1,51):
    if i%2==0:
     print(f"{i} is even")
    else:
     print(f"{i} is odd")



#Print the characters of the string "Python Rocks!" one by one.
s=input("enter the string:")
for char in s:
    print(char)

"""  
p
y
t
h
o
n"""


#Print the multiplication table of a number (e.g., 9).
num=int(input("enter the table:"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")