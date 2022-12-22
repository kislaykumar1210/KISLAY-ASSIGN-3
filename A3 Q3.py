LowerRange=int(input("Enter the lower range:"))
UpperRange=int(input("Enter the upper range:"))
tuple=[(x,x**2) for x in range(LowerRange,UpperRange+1)]
print(tuple)
