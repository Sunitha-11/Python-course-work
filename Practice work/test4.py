#1.calculate BML
def calculate_BML(weight,height):
    bml=weight/height**2
    return bml
print(calculate_BML(70,1.75))      #22.857142857142858


#2.
num=list(map(int, input("Enter numbers separated by space: ").split()))
even=list(filter(lambda x:x%2==0,num))
print("Even numbers:", even)  # Example input: 1 2 3 4 will return [2, 4]


#3.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
print(multiplication_table (5))

""" 5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50"""


#4.
def check_annagram(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
print(check_annagram("listen", "silent"))  #True

#5
def count_words(s):
    words=s.split()
    word_count=[]
    for word in words:
        


        