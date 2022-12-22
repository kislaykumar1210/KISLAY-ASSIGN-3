Month = int(input("Enter the Month"))
Day = int(input("Enter the Day"))
Year = int(input("Enter the Year"))

if 1<= Month <=12 :
    Month += 1
else:
    print("Invalid month")

if 1<= Day <=31:
    Day += 1
else:
    print("Invalid Day")

if 1800<= Year <=2025:
    Year += 1
else:
    print("Invalid Year")

print("Next Day :-", Day ,"/", Month,"/", Year)
