#1.
square=lambda n:n*n
print(square(4))    #16
print(square(7))    #49

#2.
Trueorfalse=lambda i:"True" if i%2==0 else "False"
print(Trueorfalse(12))     #True
print(Trueorfalse(13))     #False

#3.
maxof2=lambda a,b:a if a>b else b
print(maxof2(10,20))   #20
print(maxof2(10,50))     #50


#4.
productof2=lambda a,b:a*b
print(productof2(5,2))    #10

#5.
l=[(1, 3), (2, 1), (4, 2)]
sorted(l,key=lambda  i:i[1])
print(sorted(l))
"""[(2, 1), (4, 2), (1, 3)]"""

#6
l=[1,2,3,4,5,6,7,8]
num=list(filter(lambda n:n%2==0,l))
print(num) 


#7
l=[2,4,5]
squareofnum=list(map(lambda n:n*n,l))
print(squareofnum)#[2#[4, 16, 25], 

#8
s=("sunitha","sai")
sup=list(map(lambda i:i.upper(),s))
print(sup)    
#['SUNITHA', 'SAI']

#10. Return length of a string using lambda

length=lambda s:len(s)
print(length("hello"))   #5


#Check if string starts with a vowel using lambda
s="python programming"
vowel="AEIOUaeiou"
charv=list(map(lambda i:i in vowel,s))
print(charv)
"""[False, False, False, False, True, False, False, False, False, True, False, False, True, False, False, True, False, False]"""

#12. Add 10 to each element using lambda and map()
l=[1,2,3,4,5,6,7]
update=list(map(lambda i:i+10,l))
print(update)
#[11, 12, 13, 14, 15, 16, 17]

#13. Filter strings longer than 3 characters
a=["a", "the", "lamp", "cat"]
check=list(filter(lambda i: len(i)>3,a))
print(check)
#['lamp']

a=["a", "the", "lamp", "cat"]
check=list(filter(lambda i: len(i)<3,a))
print(check)   #['a']



#15.Use lambda with reduce() to calculate product
from functools import reduce
l=[1,2,3]
lup=reduce(lambda pro,items:pro*items,l)
print(lup)    #6

#16.Use lambda with filter to find multiples of 3
l=[1, 3, 4, 6, 9]
multipleof3=list(filter(lambda i:i%3==0,l))
print(multipleof3)    #[3, 6, 9]


#17. Sort words in a list by their length
words=["apple","banana","elephant","dpg"]
sortwords=sorted(words,key=lambda i:len(i))
print(sortwords)
#['dpg', 'apple', 'banana', 'elephant']






#19.Use lambda to get last digit of a number
lastdigit=lambda n:n%10
print(lastdigit(12345))     #5



#20
year=lambda n:"Leap year" if n%4==0 or n%400==0 and n%100!=0 else"Not a leap year"
print(year(2024))    #Leap year
print(year(2023))    #Not a leap year