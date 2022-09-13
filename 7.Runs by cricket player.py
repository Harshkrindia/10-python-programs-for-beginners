name = input("Enter the player's name :)")
a = int(input("Enter the 6s scored:"))
b = int(input("Enter the 4s scored:"))
c = int(input("Enter the single runs scored:"))
total = a*6 + b*4 + c*1
print("The total run scored by", name, "is", total)

if total>50:
    print("Ausum bro! Well played!")
else:
    print("Good! but there can be some improvement :) :) :)")