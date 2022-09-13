cp=float(input("Enter the cost price:-"))
sp=float(input("Enter the selling price:-"))
pp=(sp-cp)/cp*100
if pp>0 :
    print("You made a profit of",pp,"%")
elif pp<0 :
    print("You made a loss of",pp,"%")
else :
    print("You had no profit or loss")
