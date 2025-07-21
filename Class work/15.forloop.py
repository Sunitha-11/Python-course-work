n=int(input("Enter the number:"))
c=0
for i in range(2,n//2+1):
     if n%i==0:
      c=1
      break
if c:
    print("Not a prime number")
else:
    print("its a prime number")
               


#ex            
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"{n}!={fact}")


#examplw
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
