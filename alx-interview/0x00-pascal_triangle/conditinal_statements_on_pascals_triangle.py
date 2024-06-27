def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows.
    
    :params num_rows: The number of row of Pascal's Triangle.
    :return: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """
    # Step 1: Initialize the triangle as an empty list
    triangle = []

    # Step 2: Loop through rows for 0 to num_rows - 1
    for row in range(num_rows):
        # Step 3: Create a new row starting with 1
        new_row = []

        # Step 4: Loop through each position in the current row
        for col in range(row + 1):
            # Step 5: Apply conditional logic
            if col == 0 or col == row:
                # Edge element are always 1
                new_row.append(1)
            else:
                # Inner elements are the sum of the two elements above
                new_value = triangle[row-1][col-1] + triangle[row-1][col]
                new_row.append(new_value)

        # Step 6: Add the completed row to the triangle
        triangle.append(new_row)

    # Step 7: Return the generated triangle
    return triangle

# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)

