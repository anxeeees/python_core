def sum_of_square_digits(n):
    # Convert the integer 'n' to a string to iterate over the digits.
    n_str = str(n)
    # Initialize the total sum of squares to 0.
    total = 0
    # Iterate over each character in the string representation of the number.
    for digit in n_str:
        # Convert the character back to an integer.
        digit_int = int(digit)
        # Calculate the square of the digit.
        digit_square = digit_int ** 2
        # Add the square to the running total.
        total += digit_square
    # Return the total sum of squares.
    return total

# Print the sum of the squares of the digits.

n = int(input())
print(sum_of_square_digits(n))