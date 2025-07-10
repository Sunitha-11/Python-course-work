#1.Numeric data types
#a.int-integer

a=10
print(a)  #output=10
print(type(a)) #<class 'int'>


#b.Float
a=10.5
print(a) #ouput=10.5
print(type(a)) #class="float"


#complex 
a=5+10j
print(a)#output=(5+10j)
print(type(a)) #<class 'complex'>



#2.string data types
a="hello"
print(a) #output=hello
print(type(a)) #<class 'str'>



#b.list
a=[1,2,3,4,5]
print(a)     #[1, 2, 3, 4, 5]
print(type(a))    #<class 'list'>

#c.tuple
a=(1,2,3,3,4,5)
print(a) #(1, 2, 3, 3, 4, 5)
print(type(a))   #<class 'tuple'>

#3.set
a={1,2,2,2,3,4,5}
print(a)        #{1, 2, 3, 4, 5}
print(type(a))     #<class 'set'>



#4.dictionary
a ={"name":"sunitha","age":21,"rollno":927}
print(a)    #{'name': 'sunitha', 'age': 21, 'rollno': 927}
print(type(a))   #<class 'dict'>




#5.boolean type
a=100
b=200
if a > b:
    print(True)
else:
    print(False)    #False
print(type(a > b))   #<class 'bool'>



#6.none type
a=None
print(a)   #None
print(type(a))  #<class 'NoneType'>