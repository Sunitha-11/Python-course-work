try:
    file=open("demo.txt","r")
except FileNotFoundError:
    print("file is not there")
else:
    print(f"read entire content:\n{file.read()}\n")
    file.seek(0)
    print(f"read entire content:{file.readline()}\n")
    file.seek(0)
    print(f"read entire content:\n{file.readlines()}\n")
    file.close()


#
    try:
     with open("demo.txt","r+")as file:
           print(f"read entire content:\n{file.read()}\n")
           file.seek(0)
           print(f"read entire content:{file.readline()}\n")
           file.seek(0)
           print(f"read entire content:\n{file.readlines()}\n")
           file.write("\nsunitha\nsweety\nsuni")
           file.seek(0)
           print(file.read())
           file.close()
    except FileNotFoundError:
      print("file is not there")

#
try:
    with open("demo.txt","a+")as file:

         file.write("End of the file")
         file.seek(0)
         print(file.read())
         file.close()

except FileNotFoundError:
    print("file is not there")


#
try:
    with open("demo.txt","w+")as file:

         file.write("End of the file")
         file.seek(0)
         print(file.read())
         file.close()

except Exception as e:
    print("Error Occured",e)


#
import os


if not os.path.exists("Batch-31"):
    os.mkdir("batch-31")
os.rmdir("batch-31")


#
import os
import shutil

shutil.rmtree("batch-31")

#
import os
print(os.getcwd())
os.chdir("sunitha")
print(os.getcwd())


#
import os

print(os.getcwd())
print(os.listdir("."))