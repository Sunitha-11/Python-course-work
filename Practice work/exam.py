l=list(map(int,input().split()))
lnew=list(filter(lambda x:x>40,l))
print(lnew)



def prime(n, i=2):
    if n%2==0:
        return True
    else:
        return False
num=int(input())
print(prime(num))