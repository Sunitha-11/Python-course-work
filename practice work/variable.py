#basic variable assignments
product_name="Laptop"
price=45000
in_stock =True
print(product_name,price,in_stock)#outtput="Laptop 45000 True"

#Multipleassignment
a,b,c=10,20,30
print(a,b,c)#output=10 20 30



#Reassignments
name ="sunitha"
name ="sweety"
print(name) #output=sweety


#Sapping variables
a,b=10,20
a,b=b,a
print(a,b) #output=20 10




#Deleying variables
a=50
del a
print(a) #output=NameError: name 'a' is not defined