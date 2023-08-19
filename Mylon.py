#Calculate Persons Age Based on Year Of Birth.
name = str(input("Please Enter Your Good Name:"))
year = int(input("please enter the year you born:"))
print(year)
currentage = 2023 - year
months = currentage*12
print("Hello "+name+". you are %d years old." % (currentage))
print("Hello "+name+". you are %d months old." % (months))

