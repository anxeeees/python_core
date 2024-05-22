# The program starts here

def activity(day):
    if day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        return ("Study!")
    elif day == 5:
        return ("Rest!")
    else:
        return ("Leisure!")

    # Write your code here!

# Do not change anything below!

day = int(input())
print(activity(day))