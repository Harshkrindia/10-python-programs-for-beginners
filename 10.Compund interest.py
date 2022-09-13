#This program is to find the Compound Intrest by using the formula-> ci= p*(1+r/100)**t - p
p = float(input("Enter the Principal ammount:"))
r = float(input("Enter the RATE of interest:"))
t = int(input("Enter the time(in years) :"))

ci = p*(1+ r/100)**t - p
print("The Compund Interest is:= ", ci)