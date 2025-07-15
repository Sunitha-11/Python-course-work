#1.Arthmentic operators
a = 10
b = 20
print('Addition(a+b):',a+b)#Addition(a+b): 30
print('Subtraction(a-b):',a-b)#Subtraction(a-b): -10
print('Multiplication(a*b):',a*b)#Multiplication(a*b): 200
print('Division(a/b):',a/b)#Division(a/b): 0.5
print('Floor Division(a//b):',a//b)#Floor Division(a//b): 0
print('Modulus(a%b):',a%b)#Modulus(a%b): 10
print('Exponentiation(a*b):',a**b)#Exponentiation(a*b): 10000000000000000000



#2.Comparison Operators
c = 40
d = 20
print('Equal to(c==s):',c==d)#Equal to(c==s): False
print('Not Equal to(c!=d):',c!=d)#Not Equal to(c!=d): True
print('Greater than(c>d):',c>d)#Greater than(c>d): True
print('Less than(c<d):',c<d)#Less than(c<d): False
print('Greater than or Equal to(c>=d):',c>=d)#Greater than or Equal to(c>=d): True
print('Less than or Equal to(c<=d):',c<=d)#Less than or Equal to(c<=d):False




#3. Assignment Operators Example

a = 10
print("Assignment operator examples")

a += 5
print("Add and assign operator a += 5 →", a)#Add and assign operator a += 5 → 15

a -= 3
print("Subtract and assign operator a -= 3 →", a)#Subtract and assign operator a -= 3 → 12

a *= 2
print("Multiply and assign operator a *= 2 →", a)#DMultiply and assign operator a *= 2 → 24

a /= 4
print("Divide and assign operator a /= 4 →", a)#Divide and assign operator a /= 4 → 6.0

a //= 2
print("Floor divide and assign operator a //= 2 →", a)#Floor divide and assign operator a //= 2 → 3.0

a %= 3
print("Modulus and assign operator a %= 3 →", a)#Modulus and assign operator a %= 3 → 0.0

a **= 2
print("Exponentiation and assign operator a **= 2 →", a)#Exponentiation and assign operator a **= 2 → 0.0

#4.logical operators

a = True
b = False

print("a =", a) #a = True
print("b =", b)#b = False

# AND Operator
print("a and b =", a and b) #a and b = False

# OR Operator
print("a or b =", a or b)#a or b = True

# NOT Operator
print("not a =", not a)#not a = False
print("not b =", not b) #not b = True


#5.Membership operators
#list
l=[1,2,3,4,5,6,7,8,]
print(5 in l) #True
print(3 in l) #True
print( 6 in l) #True
print(10 not in l) #True
print(11 not in l) #True
print(7 in l) #True
print(6 in l) #True

#dictionary
data={"name":"sunitha","age":20,"city":"banglore"}
print("name" in data)  #True
print("city" in data)  #True
print("age" not in data)   #False
print("banglore" not in data)  #True
print("sunitha" not in data)  #True
print("20" not in data)  #True


#string
a="sunitha"
print('s' in a) #True
print('t' in a) #True
print('p' in a) #False
print('a' in a) #True
print('s' not in a) #False
print('l' not in a) #True
print('u' not in a) #False


#tuple
t={1,2,3,4,5,6,7,8,9,10}
print(5 in t) #teue
print(3 in t) #false
print(7 in t) #false
print(3 in t) #true
print(5 not in t) #False
print(5  not in t) #false


#set
s=[10,20,30,40,50]
print(10 not in s)  #false
print(200 not in s) #true
print(20 in s) #true
print(30 not in s) #false
print(50 in s) #true



#6.identity operators
#strings
s="saisunitha"
s1="sunithasai"
m=s1
print(s is s1) #false if both variables are printing to the different allocation
print(s is not s1) #True if both variables are printing to the same value
print(s in m)  #false if both variables are printing to the different allocation
print(s is not m) #true if both variables are printing to the same value

 #set
a=[1,2,3]
b=[1,2,3]
print(a is not  b) #teue
print(a is  b) #false
c=a
print(a is c) #true
print(b is not c) #true



    
#7.Bitwise Operator Example in Python

# Bitwise Operator Example in Python

# Define two numbers
x = 5  # (in binary: 0101)
y = 3  # (in binary: 0011)

# Bitwise AND
print("Bitwise AND (x & y):", x & y)  # 0101 & 0011 = 0001 -> 1

# Bitwise OR
print("Bitwise OR (x | y):", x | y)   # 0101 | 0011 = 0111 -> 7

# Bitwise XOR
print("Bitwise XOR (x ^ y):", x ^ y)  # 0101 ^ 0011 = 0110 -> 6

# Bitwise NOT (Note: this returns the complement)
print("Bitwise NOT (~x):", ~x)        # ~0101 = -(x+1) = -6
print("Bitwise NOT (~y):", ~y)        # ~0011 = -(y+1) = -4

# Bitwise Left Shift
print("Bitwise Left Shift (x << 1):", x << 1)  # 0101 << 1 = 1010 -> 10

# Bitwise Right Shift
print("Bitwise Right Shift (x >> 1):", x >> 1)  # 0101 >> 1 = 0010 -> 2