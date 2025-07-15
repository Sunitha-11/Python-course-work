#Creating Lists
#5.1 Empty List
my_list = []   ## Empty list
my_list2 = list()    ## Using list() constructor

#5.2 list with elements
numbers=[1,2,3,4,5] #list of integers
mixed = [10, "Python", 3.14, True]   #mixed data types


#nested list
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]

#using list constructor
t=list((1,2,3))


#Accessing Elements in a List
#Using Indexing (Positive & Negative)
my_list=("sunitha","sai","karunya")
print(my_list[0])  #sunitha 
print(my_list[2])   #karunya
print(my_list[-2])   #sai

#slicing
my_list=(["sunitha","sai","karunya","harika"])
print(my_list[0:2])    #['sunitha', 'sai']
print(my_list[2:4])   #['karunya', 'harika']
print(my_list[1:3])   #['sai', 'karunya']


#changing elements
n=[1,2,3,4,6]
n[3]=5
print(n)    #[1, 2, 3, 5, 6]



# Adding elements

# 1. append (add to end)
n = [1, 2, 3, 4, 6]
n.append(5)
print(n)  # [1, 2, 3, 4, 6, 5]

# 2. insert
n = [1, 2, 3, 4, 6]
n.insert(3, 13)
print(n)  # [1, 2, 3, 13, 4, 6]

#Extend()
n = [1, 2, 3, 4, 6]
n.extend([3,13,10,11,12])
print(n)    #[1, 2, 3, 4, 6, 3, 13, 10, 11, 12]

#Removing elements()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.remove(2)
print(n)   #[1, 3, 5, 6, 7, 8, 6, 3, 3, 4] 

#pop()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.pop(2)
print(n)   #[1, 2, 5, 6, 7, 8, 6, 3, 3, 4] 


n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.pop()
print(n)    #[1, 2, 3, 5, 6, 7, 8, 6, 3, 3] 

#clear()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.clear()
print(n)     #[]


#del numbers()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
del n[3]
print(n)    #[1, 2, 3, 6, 7, 8, 6, 3, 3, 4]  


#count()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
print(n.count(3))    #3


#sort()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.sort()
print(n)    #[1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8] 

#reverse()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
n.reverse()
print(n)     #[4, 3, 3, 6, 8, 7, 6, 5, 3, 2, 1]

#max()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
print(max(n))    #8


#min()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
print(min(n))   #1


#sum()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
print(sum(n))    #48

#len()
n = [1, 2, 3, 5, 6, 7, 8, 6, 3, 3, 4]
print(len(n))    #11


#any()
values = [0, "", None, False]
print(any(values))  #false

#all()
values = [0, "", None, False]
print(all(values))     #false
