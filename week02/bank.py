#Weekly Task 02

#Prompt the user and read in two money amounts (in cent)
amount1 = int(input("Enter amount1(in cent): "))
amount2 = int(input("Enter amount2(in cent): "))

#Add the two amounts and convert to decimal format (euro)
total = (amount1+amount2)/100

#Print answer with euro included
print (f"The sum of these is €{total}")