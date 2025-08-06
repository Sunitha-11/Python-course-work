#1.positional arg()
def student_details(name,rollno,marks,grade,course):
   print('Name:',name)
   print('Rollno:',rollno)
   print('Marks:',marks)
   print('Grade:',grade)
   print('Course:',course)
    
    
name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")



student_details(name,rollno,marks,grade,student_course)
"""output=
Name: sun itha
Rollno: 11
Marks: 100
Grade: A
Course: sql """

student_details("sweety",12,100,"A","Python")

"""
Name: sweety
Rollno: 12
Marks: 100
Grade: A
Course: Python """




#2.keyword arg()
def student_details(name,rollno,marks,grade,course):
   print('Name:',name)
   print('Rollno:',rollno)
   print('Marks:',marks)
   print('Grade:',grade)
   print('Course:',course)
    
    
name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")



student_details(name=name,rollno=rollno,marks=marks,grade=grade,course=student_course)

"""
Name: kumar
Roll no: 20
Marks: 70
Grade: C
Course: DS"""

student_details(name=name,marks=marks,rollno=rollno,course=student_course,grade=grade,)

"""
Name: kumar
Rollno: 20
Marks: 70
Grade: C
Course: DS"""

student_details(name="sai",rollno=20,marks=100,grade="A",course="java")

"""
Name: sai
Rollno: 20
Marks: 100
Grade: A
Course: java """



#3.default arg()
def student_details(name,rollno,marks=0,grade="F",course="python"):
   print('Name:',name)
   print('Rollno:',rollno)
   print('Marks:',marks)
   print('Grade:',grade)
   print('Course:',course)
    
    
name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
course=input("Course: ")

student_details(name,rollno)

"""
Name: suni
Rollno: 10
Marks: 0
Grade: F
Course: python"""

student_details(name,rollno,marks)
"""
Name: suni
Rollno: 10
Marks: 100
Grade: A
Course: python"""

student_details(name,rollno,marks,grade)
"""
Name: suni
Rollno: 10
Marks: 100
Grade: A
Course: python"""

student_details(name,rollno,marks,grade,course)
"""
Name: suni
Rollno: 10
Marks: 100
Grade: A
Course: python"""


