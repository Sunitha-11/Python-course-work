#Dictionary()
student={"name":"sunitha","age":"19","course":"python"}
print(student)      #{'name': 'sunitha', 'age': '19', 'course': 'python'}

#Accessing the values
student={"name":"sunitha","age":"19","course":"python"}
print(student.get("city","not available"))      #not available

#Adding and updating iitems
student["age"] =22
student["city"]="New york"
print(student)       #{'name': 'sunitha', 'age': 22, 'course': 'python', 'city': 'New york'}


#removing items
age=student.pop("age")
print(age)
print(student)         #{'name': 'sunitha', 'course': 'python', 'city': 'New york'}


#deleting items()
del student["course"]
print(student)      #{'name': 'sunitha', 'city': 'New york'}


# dict update
student2={"name":"sunitha","age":19,"course":"python","city":"new york"}
student2["age"] = 25
print(student2)  # prints {'city': 'banglore'}

#dictclear()
student = {"name": "sunitha", "age": 19, "course": "python"}
print(student.clear())  # clears dictionary
print(student)  # prints empty dictionary {}


#3.Dictionary Built-in Methods
#3.1.dict.keys()
dict5 = {'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE', 'city': 'Mancherial'}
print(dict5.keys()) #dict_keys(['name', 'age', 'course', 'city'])
print(dict5.values()) #dict_values(['Durgam Revathi', 24, 'CSE', 'Mancherial'])
print(dict5.items()) #dict_items([('name', 'Durgam Revathi'), ('age', 24), ('course', 'CSE'), ('city', 'Mancherial')])


#Built-in Function For Dictionaries
#4.1.len,sorted,max,min
dict6 = {1:'a',2:'b',3:'c',4:'d'}
print(len(dict6)) #3
print(sorted(dict6)) #['Key1', 'key2', 'key3']
print(max(dict6)) #key3
print(min(dict6)) #key1



#Nested Dictionaries
dict7 = { "Revathi":{'age': 24, 'course': 'CSE', 'city': 'Mancherial', 'year': 4},"Sony":{'age': 19, 'course': 'IT', 'city': 'Jannaram', 'year': 2}}
print(dict7["Revathi"]["city"]) #Mancherial
print(dict7["Sony"]["age"]) #19