count = 0
MyString = str(input("Enter your String"))
MyChar = str(input("Enter the word you want to count"))

for i in MyString:
    if i==MyChar:
        count += 1

print(count)
