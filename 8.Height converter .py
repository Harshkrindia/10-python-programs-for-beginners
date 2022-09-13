#This program is can convert hieghts from cm to m and cm
a = float(input("Enter your hieght in cm::"))
b = 0
while a>=100:
    b = b+1
    a = a-100
print("The hieght of the person is ", b, "m ", a, "cm")