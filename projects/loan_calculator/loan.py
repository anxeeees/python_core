import math

loan_principal = 'Loan principal: 1000'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
final_output = 'The loan has been repaid!'
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)

# write your code here

print("Enter the loan principal:")
principal = int(input())  # 1000
print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
choice = input()

if choice == 'm':
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    result = principal / monthly_payment
    result = math.ceil(result)
    print("")
    if result > 1:
        print("It will take " + str(int(result)) + " months to repay the loan")
    else:
        print("It will take " + str(int(result)) + " month to repay the loan")
elif choice == 'p':
    print("Enter the number of months:")
    months = int(input())
    result = principal / months
    if result % 2 == 0:
        print("Your monthly payment = "+str(result))
    else:
        result = math.ceil(result)
        new = principal - ((months - 1) * result)
        print("Your monthly payment = "+str(result) + " and the last payment = "+str(new))