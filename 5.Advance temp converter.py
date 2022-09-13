#This program allows you to convert the temperature from celsius to fahrenheit and vice versa
#Credit goes to ⭐Prashant and Harsh
print('\n' "⭐⭐xxxxxxxxxx Welcome to the MATRIX xxxxxxxxxxxx⭐⭐")
print("If you want to convert from C° to F° ENTER 1 or If u want to convert from F° to C° ENTER 2")
a=str(input("Enter your choice:"))
if a=="1":
    b=float(input("Enter the Value in C°:-"))
    f=b*9/5+32
    print(b,"C° =",f,"F°")
elif a=="2":
    b=float(input("Enter the Value in F°:-"))
    c=(b-32)*5/9
    print(b,"F° =",c,"C°")
else:
    print("You have entered an in valid code")
print("_____________________⭐ END ⭐ ____________________")
