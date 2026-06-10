def print_pascal_triangle(n):
    """
    Print Pascal's Triangle with n layers (rows).
    
    Pascal's Triangle is a triangular array where each number is the sum of the two numbers 
    directly above it. It has many applications in combinatorics, probability theory, and algebra.
    
    Args:
        n (int): Number of layers/rows to print
    
    Example:
        For n=5, the output will be:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
    """
    # Iterate through each row of the triangle
    for i in range(n):
        # Print leading spaces for triangle formatting
        # Each row needs (n - i - 1) spaces to center-align the triangle
        print(' ' * (n - i - 1), end='')
        
        # Calculate and print values for current row
        # Start with 1 (first element in every row is always 1)
        value = 1
        
        # Iterate through each position in the current row
        for j in range(i + 1):
            # Print the current value followed by a space
            print(value, end=' ')
            
            # Calculate next value using binomial coefficient formula
            # C(i, j+1) = C(i, j) * (i - j) / (j + 1)
            # This efficiently computes the next value without storing previous rows
            value = value * (i - j) // (j + 1)
        
        # Move to next line after completing the current row
        print()


if __name__ == "__main__":
    # Demonstration: Print Pascal's Triangle with 5 layers
    print("Pascal's Triangle with 5 layers:")
    print()
    print_pascal_triangle(5)
