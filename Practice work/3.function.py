#1. Add Two Numbers
def add(a,b):
    return a+b
print(add(5,10))  #15



#2.Square a Number

def square_of_num(n):
    return n*n
print(square_of_num(4))    #16


#3. Area of a Circle
def circle(r):
    return 3.14*r*r
print(circle(10))        #314.0


#4 Greet the User
def greet(name):
    return f"hello {name}!"
print(greet("sunitha"))   #hello sunitha!


#5 Convert Celsius to Fahrenheit
def celsius_to_fohrenheit(c):
    return (c*9/5)+32
print(f"fohrenheit is {celsius_to_fohrenheit(37)}")    #fohrenheit is 98.6



#6. Multiply Three Numbers
def multiply_three_numbers(a,b,c,d):
    return a*b*c*d
print(multiply_three_numbers(2,3,4,5))    #120


#7.Calculate Simple Interest
def simple_interest(p,t,r):
    return p*t*r/100
print(simple_interest(1000,2,5))     #100.0


#8. Find Length of a String

def  string_length(s):
    return len(s)
print(string_length("sunitha"))     #7



#9. Append to a List
def append_to_list(lst,item):
    lst.append(item)
    return lst
print(append_to_list([1, 2, 3], 4))  #[1, 2, 3, 4]



#10. Double Each Element in a List
def double_the_number(lst):
    return[lst*2 for lst in lst]
print(double_the_number([1,2,3,4,5]))    #[2, 4, 6, 8, 10]


#11. Sort a List
def sort_list(lst):
    return sorted(lst)
print(sort_list([3, 1, 4, 2]))    #[1, 2, 3, 4]


#12. Clear a List Inside Function
def clear_list(lst):
    lst.clear()
    return lst
print(clear_list([1, 2, 3, 4]))    #[]



#13.update dictionary value
def update_dict_value(d, key, value):
    d[key] = value
    return d
print(update_dict_value({'a': 1, 'b': 2}, 'b', 3))  #{'a': 1, 'b': 3}


#14. Remove Element from List by Value
lst=list(map(int,input("enter thr number:").split()))
def remove_element(lst,value):
    if value in lst:
        lst.remove(value)
        return lst
    else:
        return "Value not found in the list"
print(remove_element(lst, 3))  # Example input: [1, 2, 3, 4] and value 3 will return [1, 2, 4]



#15.Add Key to Dictionary
# Function to add a key-value pair to dictionary
def add_key_value(my_dict, key, value):
    my_dict[key] = value
    return my_dict

# Initial dictionary
my_dict = {'x': 10}

# Take input from user
key = input("Enter new key: ")
value = int(input("Enter new value: "))

# Call the function
updated_dict = add_key_value(my_dict, key, value)

# Display result
print("Updated dictionary:", updated_dict)


#16. Increment All Values in Dictionary
def  increment_dict_values(d, increment):
    return {k: v + increment for k, v in d.items()}
print(increment_dict_values({'a': 1, 'b': 2}, 3))  # {'a': 4, 'b': 5}



#17. Factorial of a Number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from user
num = int(input("Enter a number: "))

# Call the function
fact = factorial(num)

# Display result
print(f"Factorial of {num} is: {fact}")



#18. Fibonacci Number (Nth Term)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Take input from user
term = int(input("Enter term number: "))

# Call the function
fib_num = fibonacci(term)

# Display result
print(f"Fibonacci number is: {fib_num}")


#19. Sum of First N Natural Numbers
def sum_of_natural_numbers(n):
    return n*(n+1)//2
print(sum_of_natural_numbers(10))  #55

#20. Reverse a String Using Recursion
def revers_string(s):
    if len(s)==0:
        return s
    else:
        return s[::-1]
print(revers_string("hello"))  #olleh



##21. Power of a Number (a^b using recursion)
def pwwer(a,b):
    if b==0:
        return 1
    else:
        return a * pwwer(a, b - 1)
print(pwwer(2, 3))  #8

#22.sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"Sum of digits in {num} is: {result}")


#23.Check Palindrome String Using Recursion
def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
print(palindrome("radar"))  #True


#24. GCD of Two Numbers Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(8,12))  


#25. Maximum of Three Numbers Using max()
def max_of_num(a,b,c):
    return max(a,b,c)
print(max_of_num(10,20,30))  #30


#26. Sort a List Using sorted()
def sort_list(lst):
    return sorted(lst)
print(sort_list([3, 1, 4, 2]))  #[1, 2, 3, 4]


#27.Sum of Elements Using sum()
def sum_of_elements(lst):
    return sum(lst)
print(sum_of_elements([1, 2, 3, 4]))  #10

#28. Find Data Type Using type()
def find_data_type(value):
    return type(value)
print(find_data_type(10))  #<class 'int'>


#29. Print Even Numbers up to N
def print_even_numbers(n):
    return [i for i in range(2, n + 1, 2)]
print(print_even_numbers(20))  #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#30. Return List of Squares
def list_of_squares(n):
    return [i**2 for i in range(1, n + 1)]
print(list_of_squares(5))  #[1, 4, 9, 16, 25]


#31. Check if Number is Prime
def is_prime(n):
    if n%2!=0:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return n == 2
print(is_prime(29))  #True


#32. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello World"))  #3


#32. Count Vowels in a String
l=lambda x:x*2
print(l(5)) #10


#34. Square List Using map() and Lambda
s=list(map(lambda x: x**2))
print(s([1, 2, 3, 4, 5]))  #[1, 4, 9, 16, 25]


#35. Filter Even Numbers Using filter() and Lambda
s1=list(filter(lambda x:x%2==0))
print(s1([1, 2, 3, 4, 5, 6]))  #[2, 4, 6]


#36. Sort Tuples by Second Value Using Lambda
s=sorted(key=lambda x:x[1])
print(s([(1, 3), (2, 1), (4, 2)]))  #[(2, 1), (4, 2), (1, 3)]



