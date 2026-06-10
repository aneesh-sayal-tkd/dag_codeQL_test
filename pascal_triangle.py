def print_pascal_triangle(n):
    """
    Print Pascal's Triangle with n layers (rows).
    
    Args:
        n (int): Number of layers/rows to print
    """
    for i in range(n):
        # Print leading spaces for triangle formatting
        print(' ' * (n - i - 1), end=''
        
        # Calculate and print values for current row
        value = 1
        for j in range(i + 1):
            print(value, end=' ')
            # Calculate next value using binomial coefficient formula
            # C(i, j+1) = C(i, j) * (i - j) / (j + 1
            value = value * (i - j) // (j + 1)
        
        print()  # New line after each row


if __name__ == "__main__":
    # Print Pascal's Triangle with 5 layers
    print("Pascal's Triangle with 5 layers:")
    print()
    print_pascal_triangle(5)
