def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows.

    :param num_rows: The number of rows of Pascal's Triangle to generate.
    :return: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """
    # Step 1: Initialize the triangle as an empty list
    triangle = []

    # Step 2: Loop through rows from 0 to num_rows - 1
    for row in range(num_rows):
        # Step 3: Create a row starting with 1
        new_row = [1]

        # Step 4: Fill in the middle elements of the row if row > 0
        if row > 0:
            new_row.extend([triangle[row-1][col-1] + triangle[row-1][col] for col in range(1, row)])
            # Step 5: End each row with 1
            new_row.append(1)

        # Step 6: Add the completed row to the triangle
        triangle.append(new_row)

    # Step 7: Return the generated triangle
    return triangle

# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
