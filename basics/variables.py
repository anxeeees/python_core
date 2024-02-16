name = "Ester"
name2 = 'Ester'

print(name)
print(name2)
print("hello world")
print("hello "+name2)

#printing data type of variable
print(type(name2))

#printing name
first_name = "Ester"
last_name = "Stankovska"
full_name = first_name + " " + last_name
print(full_name)

age = 21
age +=1
print(age)

# in python u cannot write string + different data type
# this wont work:  print("Your age is" + age)

# this will work
print("Your age is " + str(age))

#float
height = 250.5
print(height)
print("Your height is " + str(height))

human = True
print(human)
print("Are you human? "+str(human))