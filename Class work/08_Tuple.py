#7.Tuple
#Empty tuple()
Empty_tuple=()

#single tuple()
single_tuple=(5,)

#multiple element tuple()
my_tuple=(1,"apple",3.5)

#indexing
my_Tuple=(10,20,30,40)
print(my_Tuple[2])     #30

#Negative indexing
my_Tuple=(10,20,30,40)
print(my_Tuple[-2])    #30


#slicing()
my_Tuple=(10,20,30,40)
print(my_Tuple[1:4])       #(20, 30, 40)

#3.operations on tuples
Tuple1 = (2, 3)
Tuple2 = (3, 4)
new_tuple = Tuple1 + Tuple2
print(new_tuple)       #(2, 3, 3, 4)



#REpetition
my_Tuple=(1,2)
print(my_Tuple*3)      #(1, 2, 1, 2, 1, 2)


#Membership testing
my_Tuple=(1,2,3,4,5)
print(1 in my_Tuple)    #True
print(3 not in my_Tuple)    #False

#Tuple unpacking
my_Tuple=(1,2,3)
a,b,c=my_Tuple
print(a,b,c)   #1 2 3

#4,Tuple methods
#count()
a=(1,2,3,4,5,2,)
print(a.count(1))      #1



#index()
a=(1,2,3,4,5)
print(a.index(3))      #2

#5.Built-in Functions for Tuples
#len()
a=(1,2,3,4,5)
print(len(a))   #5

#max()
a=(1,2,3,4,5)
print(max(a))    #5

#min()
a=(1,2,3,4,5)
print(min(a))    #1


#sum()
a=(1,2,3,4,5)
print(sum(a))    #15

#Tuple iterable
Tuple = (1, 2, 3, 4, 5)
print(Tuple[1:5])  # Output: (2, 3, 4, 5)


#nested Tuple()
nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 100
print(nested_tuple)      #(1, [100, 3])