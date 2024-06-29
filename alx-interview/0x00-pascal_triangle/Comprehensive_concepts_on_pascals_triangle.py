#!/usr/bin/env python3

def generate_pascals_triangle_optimized(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows with optimized space complexity

    :param num_rows: The number of rows of Pascal's Triangle. Must be a non-integer.
    :return: A list of lists, where each inner list represents a row of Pascal's Triangle.
    :raises ValueError: If num_rows is not a non-negative integer.
    """
    # Step 1: Input validation
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be a non-negative integer")
    
    # Step 2: Initialize the triangle as an empty list
    triangle = []

    # Step 3: Loop through rows from 0 to num_rows - 1
    for row in range(num_rows):
        # Step 4: Create a new row with 'None' placeholders
        new_row = [None for _ in range(row + 1)]

        # Step 5: Set the first and last elements to 1
        new_row[0], new_row[-1] = 1, 1

        # Step 6: Fill in the inner elements
        for col in range(1, row):
            new_row[col] = triangle[row-1][col-1] + triangle[row-1][col]

        # Step 7: Add the completed row to the triangle
        triangle.append(new_row)

    # Step 8: Return the generated triangle
    return triangle

# Example usage with error handling
try:
    num_rows = 5
    triangle = generate_pascals_triangle_optimized(num_rows)
    for row in triangle:
        print(row)
except ValueError as e:
    print(f"Error: {e}")
