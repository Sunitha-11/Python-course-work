#var=lamba para/args:exp
u=lambda n:n+10
print(u(10))     #20


cube=lambda n:n**3
print(cube(2))    #8

add=lambda a,b:a+b
print(add(10,20))     #30


greater=lambda a,b:a if a>b else b
print(greater(10,30))      #30



evenorodd=lambda n:"even"if n&2==0 else "odd"
print(evenorodd(10))    #odd
print(evenorodd(13))   #even


sumof3=lambda a,b,c:a+b+c
print(sumof3(10,20,30))      #60


#using map()
s="python programming"
changstr=list(map(lambda i:i.upper(),s))
print(changstr)

"""['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']"""


s="python programming"
asci=list(map(lambda i:ord(i),s))
print(asci)
"""[112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]"""



vowel="aeiouAEIOU"
chv=list(map(lambda i:"*"if  i in vowel else "0",s))
print(chv)
"""['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']"""


l=[1,2,3,4,5,6,7,8,9,10]
lup=list(map(lambda i:i+1,l))
print(lup)
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


t=(10,20,30,40,12,31)
tup=list(map(lambda i:i//10,t))
print(tup)
#[1, 2, 3, 4, 1, 3]

