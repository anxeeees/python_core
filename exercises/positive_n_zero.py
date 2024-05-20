# Function to test if a number is Positive, Negative, or Zero
def check_num(n):
    if n > 0:
        print("Positive")
    if n < 0:
        print("Negative")
    if n == 0:
        print("Zero")
    # Define your if-statement here to check the value of n and return "Positive", "Negative", or "Zero"

check_num(int(input()))
# Testing your function with inputs
# Remember to call the check_num function with a number as argument.