num = int(input("please input a number :"))
print(f"please input a number :{num}")
if(num%2):
    print("this is odd")
else:
    print("this is even")
    
ch = input("please input your student ID first character :")
print(f"please input a number :{ch}")
id = input("please input your student ID last 8 numbers :")
print(f"please input a number :{id}")

if(id%2):
    print("this is odd")
else:
    print("this is even")
    
print(f"your student ID is :{ch}{id}")