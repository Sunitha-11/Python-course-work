#elif example for hrs and mins()
hr,mins=list(map(int,input("Enter the time HH:MM").split(":")))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print("its high time to sleep")
    elif hr>=4 and hr<12:
        print("good morning,have a great day")
    elif hr>=13 and hr<16:
        print("good afternoon,have a good lunch")
    elif hr>=16 and hr<20: 
        print("good evening")
    elif hr>=20 and hr<24:
        print("good night,sweet dreams")
else:
    print("its not correct time")




#3.seats available in bus()
seats = {
    "L1": True,
    "L2": False,
    "L3": True,
    "L4": False,
    "L5": True,
}

seatno = input("Enter the seat no to check its availability: ").upper()
if seatno in seats:
    if seats[seatno]:
        print("Already booked ,try other number: ")
    else:
     print("Available seat book,Hurry uo")
else:
    print("Enter correct seat number")




#4.example for product discount()
data={
    "Watches":{"discount":10,"brands":["titan","fasttrack"]},
    "facewash":{"discount":30,"brands":["mamaearth","clean and clear"]},

}
print(data.keys)
pro=input("Enter the cat: ")
if pro in data:
    print(f"{data[pro] ["discount"]}% discount is going on brands :{data[pro]["Brandss"]}")
else:
    print("product is out of stock")




#5.movie checking movies seen by kids or not()
movies={
    "salar":{"kids":True},
    "rajarani":{"kids":False},
    "Arjun reddy":{"kids":False},
    "Littlestars":{"kids": True},

}
print("Welcome to hotstar".center(30,"="))
movie =input("Enter the movie: ").title()
if movie in movies:
    if movies[movie]["kids"]:
        print(f"Good selection ,you can watch with your family\n{movie}.....")
    else:
        print(f"Adult movie.kids are not allowd ,\n{movie}...")
else:
    print(f"{movie} is not available ")




#6 checking the place go with visa and passport or not()
data={
    "INDIA":("passport"),
    "NEPAL":("passport"),
    "CANADA":("passport","visa"),
    "ENGLAND":("passport","visa"),

}

from_place=input("Enter the place you want to go: ")
to_place=input("Enter the place you want to go: ").upper()
if to_place in data:
    if len(data[to_place])==1:
        print(f"Great .you only need passport to visit {to_place}")
    else:
        print(f"Great .you only need passport and visa to visit {to_place}")
else:
    print("data is not available")






