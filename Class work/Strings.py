#Defining strings
#concatenation
s1="sunitha"
s2="sweety"
s3="suni"
s=s1+s2+s3
print(s)  #output=sunithasweetysuni

#repetition
s="sunitha"
print(s*3) #output=sunithasunithasunitha



# indexing
s = "sunitha"
print(s[3])   # output = i
print(s[-1])  # output = a


#slicing
s3="suni"
print(s3[0:3]) #outputput=sun
print(s3[2:]) #ni
print(s3[:5]) #suni

#Membership operators
text="sunitha"
print('sunitha' in text) #True
print('sunitha' in text) #True


#length()
text="sunitha"
print(len(text))   #7


#max() and min()
print(max("SUNitha"))     #t
print(min("SUNitha"))   #N


#sorted
print(sorted("sunithasai"))   #['a', 'a', 'h', 'i', 'i', 'n', 's', 's', 't', 'u']


#chr() and ord()
print(ord("s"))  #115
print(chr(97))  #a


#1. Case Conversion Methods
#upper()
s="sunitha"
print(s.upper())    #SUNITHA


#lower()
s="EERLA"
print(s.lower())    #eerla


#capitalize()
s="eerla"
print(s.capitalize())    #Eerla



#title()
s="sunitha is a good girl"
print(s.title())   #Sunitha Is A Good Girl


#swapcase()
s="sunitha is a good girl"
print(s.swapcase())     #SUNITHA IS A GOOD GIRL


#casefold()
s="sunitha"
print(s.casefold())     #sunitha


#2.Alignmrnt and formatting methods
#center width()
s="sunitha"
print("sunitha".center(10,"*"))     #*sunitha**


#ljust()
s="sunitha"
print("sunitha".ljust(5,"*"))   #"**sunitha"


#rjust()
s="sunitha"
print("sunitha".rjust(5,"*"))       #"sunitha**"


#zfill
a="42"
print(a.zfill(6))     #000042


#3.search and find methods
#find
a="hello"
print("hwllo".find("o"))    #4

#rfind
a="hello"
print("hwllo".rfind("l"))     #3

#index()
a="hello"
print("hwllo".index("l"))      #2


#index()
a="hello"
print("hwllo".rindex("l"))   #3


#count()
a="welcome"
print("welcome".count("e"))   #2



#4.string testing methods
#startswith
a="sunitha"
print("sunitha".startswith("sun"))     #True

#endswith
a="sunitha"
print("sunitha".endswith("ha"))       #True

#isalpha()
a="sunitha"
print("sunitha".isalpha())     #True


#isalnum()
a="sunitha123"
print("sunitha".isalpha())      #TRUE


#islower()
a="sunitha"
print("sunitha".islower())     #True


#isupper()
a="SWEETY"
print("SWEETY".isupper())     #True


#isspace()
a=" "
print(" ".isspace())    #True


#istitle()
a="Hello world"
print("Hello world".istitle())    #False



#isidentifier()
a="1MYVAR"
print("1MTVAE".isidentifier())     #False


#5.Replace & Modify Methods
#replace()
b="sunitha"
print("sunitha".replace("n","m"))    #sumitha


#translate()
b="suni"
print("suni".translate(str.maketrans("u","o")))    #soni

#maketrans()
a="python"
print("python".maketrans("aon","%#5"))   #{97: 37, 111: 35, 110: 53}


#6.splitting and joining methods
#split()
a="s,u,n"
print("s,u,n".split("."))     #['s,u,n']


#rsplit()
a="s,u,n"
print("s,u,n".rsplit("."))     #['s,u,n']


#splitlines()
a="sunitha\nsweety"
print("sunitha\nsweety".splitlines())    #['sunitha', 'sweety']

#join()
a="sunitha","sweety"
print(" ".join(("sunitha","sweety")))   #"sunitha sweety"


#partition()
a="apple-pie"
print("apple-pie".partition("-"))    #('apple', '-', 'pie')




#rpartition()
a="apple-pie"
print("apple-pie".rpartition("-"))   #('apple', '-', 'pie')



#7.Whitespace & Trimming Methods
a="hello "
print("hello ".strip())          #hello



#lsstrip()
a="---hello"
print("--hello".lstrip("-"))    #"hello"



#rstrip()
a="hello--"
print("--hello".rstrip("-"))      #--hello


#8.encoding and decoding()
#encoding()
a="hello"
print("hello".encode("utf-8"))    #b'hello'



#decoding
a=b'hello'
print(b'hello'.decode("utf-8"))     #hello
