def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows using list comprehensions.

    :params num_rows: The number of rows of Pascal's Triangle to generate.
    :return: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """

    triangle = []

    for row in range(num_rows):
        # Create the new row
        new_row = [1] # Start each row with 1

        # Fill in the middle elements using list comprehension if row > 0
        if row > 0:
            new_row.extend([triangle[row-1][col-1] + triangle[row-1][col] for col in range(1, row)])
            new_row.append(1) # End each row with 1

        triangle.append(new_row)
    
    return triangle

# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
