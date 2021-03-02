MyList = [1, 22, 45, 90, 910, 555, 101]

user_input = int(input("enter the value: "))

for ml in MyList:
    if user_input == ml:
        print("we got the match")
        break
else:
   print("No match")
print("outside of Loop")