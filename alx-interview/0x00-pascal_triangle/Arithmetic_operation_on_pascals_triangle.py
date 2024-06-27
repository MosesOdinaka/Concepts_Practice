#!/usr/bin/python3
def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows.

    :param num_rows: The number of rows of Pascal's Triangle to generate.
    :return: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """

    # Step 1: Initialize the triangle as an empty list
    triangle = []

    # Step 2: Loop through rows from 0 to num_rows - 1
    # Outer Loop Through Rows:
    for row in range(num_rows):
        # Step 3: Create a new row starting with 1
        new_row = []

        # Step 4: Loop through each position in the current row
        # Inner Loop to Fill Row
        for col in range(row + 1): # Iterates through each position in the current row
            # Step 5: Apply conditional logic
            # If the position is at the edge (first or last element), append 1.
            if col == 0 or col == row:
                # Edge elements are always 1
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
