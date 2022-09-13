#Find the final velocity after thing the inputs- initial velocity,acceleration
# and time by using the formula v=u+at
u = float(input("Enter you initial velocity:"))
a = float(input("Enter the acceleration:"))
t = float(input("Enter the time(in decimal)"))

v = u + a*t
print("The final velocity of the vehicle is:", v)