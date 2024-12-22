# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through the rows
while row < size:
    # Use a for loop to print asterisks for each column in the current row
    for col in range(size):
        print("*", end="")  # Print an asterisk without moving to a new line
    
    # After completing one row, print a newline character
    print()

    row += 1
