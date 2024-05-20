print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is "+str(age)+"; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")

number = int(input())
counter = 0
while counter <= number:
    print(str(counter) +" !")
    counter += 1
print("Let's test your programming knowledge.\n"
      "Why do we use methods?\n"
      "1. To repeat a statement multiple times.\n"
      "2. To decompose a program into several small subroutines.\n"
      "3. To determine the execution time of a program.\n"
      "4. To interrupt the execution of a program.")

answer_str = int(input())
answer = True
while answer:
    if answer_str == 2:
        print("Congratulations, have a nice day!")
        answer = False
    else:
        print("Please, try again.")
        answer_str = int(input())