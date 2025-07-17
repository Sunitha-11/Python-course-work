#elif
hr,min=list(map(int,input("Enter the time HH:MM").split(":")))
if hr>=0 and hr<=24 and min>=0 and min<=60:
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