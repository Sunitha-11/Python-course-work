moves=34
winningpoint=int(input("enter the winning point:"))
while moves>0:
    if moves==winningpoint:
        print("congrats!!,you won the game")
        break
    print(f"{moves} are left,ypu have chance to win thwe game")
    moves-=1
else:
    print("Game over,try again")    



#list
l=[1,2,3,4,5]
ind=0
while ind<len(l):
    print(l(ind))
    ind+=1


#while
n=int(input())
s=0
while n>0:
    s+=(n%10)
    n//=10
print(s)



#palindrome
n=int(input())
temp=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n//=10
    if rev==temp:
        print("Palindrome")
    else:
        ("not a palindrome")


    
n=input()
full=n(len)-1
length=len(n)//2
ind=0
while ind<=length:
    if n(ind)!=n(full):
        print("not a palindrome")
        ind+=1
        

