MyGrade = int(input("Enter the grade"))

if 4<= MyGrade <=10 :
    if MyGrade == 10:
            print("Your Grade is ‘A+’ and Outstanding Performance")
    elif MyGrade == 9:
            print("Your Grade is ‘A’ and Excellent Performance")
    elif MyGrade == 8:
            print("Your Grade is ‘B+’ and Very Good Performance")
    elif MyGrade == 7:
            print("Your Grade is ‘B' and Good Performance")
    elif MyGrade == 6:
            print("Your Grade is ‘C+’ and Average Performance")
    elif MyGrade == 5:
            print("Your Grade is ‘C’ and Below Average Performance")
    elif MyGrade == 4:
            print("Your Grade is ‘D’ and Poor Performance")
    else:
        pass
else:
     print("Enter a Valid Grade")
