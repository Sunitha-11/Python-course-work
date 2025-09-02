#2.basic Exception
try:
    a=12/0
    b=int(input("enter the int:"))
    c=3+6
    d={1:2,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+m
except ZeroDivisionError:
    print("you can't divide by zero!")


"""utput
error occured"""

#3.multiple except blocks
try:
    a=12/0
    b=int(input("enter the int:"))
    c=3+6
    d={1:2,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+m


except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("please enter the proper datatype")
except TypeError:
    print("we cant add 2 diff types")
except KeyError:
    print("we dont have that key")
except IndexError:
    print("we dont have that index")
except NameError:
    print("please def the var")



#4.mmultiple exception
try:
    a=12/0
    b=int(input("enter the int:"))
    c=3+6
    d={1:2,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+m
except(ZeroDivisionError,ValueError,TypeError,KeyError,IndexError,NameError)as e:
    print(f"Error occured: {e} ")


#5.else clause
try:
    a=12/6
    b=int(input("enter the int:"))
    c=3+6
    d={1:2,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    e=3
    c=a+m
except Exception as e:
    print( f"error occured:{e}")
else:
    print("error frees")

    

#6.Final clause
try:
    products={"iphone":20000,"samsung":20000,"oneplus":30000}
    search=input()
    print(products[search])
except Exception as e:
    print( f"error occured:{e}")
finally:
    print("end of the program")


#7.Raising Exception
try:
   ids=["pfs1","pfs2","pfs3"]
   new="pfs4"
   if not new.startswith("pfs"):
       raise Exception("it needs to start with pfs")
   ids.append(new)
   print(ids)
       
except Exception as e:
    print( f"error occured:{e}")
else:
    print("error frees")
finally:
    print("end of the program")



#9.Nested Exception
try:
  a=int(input())
  b=int(input())
  try:
      c=a/b
  except:
       print( f"error occured:{e}")
      
except Exception as e:
    print( f"error occured...........:{e}")
else:
    print("error frees")
finally:
    print("end of the program")


