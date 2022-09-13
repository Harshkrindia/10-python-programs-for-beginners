#This program is to find the marks and percentage of 5 different subjects
a = int(input("Enter the marks of Maths:"))
b = int(input("Enter the marks of Science:"))
c = int(input("Enter the marks of S.ST:"))
d = int(input("Enter the marks of French:"))
e = int(input("Enter the marks of AI:"))
#Now sum the total marks and print the marks and percentage
sum = a+b+c+d+e
percentage = (sum/500)*100

print("The sum is= ", sum)
print("The percentage is= ", percentage)

