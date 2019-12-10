age_of_oldboy = "56"
count = 0
#  for i in range(3):
   #print(count)
while count < 3:
    age = int(input("age:"))
    if age == int(age_of_oldboy):
        print("yes you got it!")
        break
    elif age < int(age_of_oldboy):
        print("think bigger")
    else:
        print("think smaller")
    count += 1
    if count == 3:
        continue_confirm = input("Do you want to keep guessing? ")
        if continue_confirm != "n":
            count = 0

#else:
#    print("fuck off")