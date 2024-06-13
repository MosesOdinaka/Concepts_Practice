def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows.

    :param num_rows: The number of rows of Pascal's Triangle to generate.
    :return: A list of list, where each inner list represents a row of Pascal's Triangle.
    """
    # Initialize the triangle as an empty list
    triangle = []

    # Iterate through each row from 0 to num_row - 1
    for row in range(num_rows):
        # Start each row with a list containing one element '1'
        new_row = [1]

        # Fill in the middle elements of the row
        if row > 0:
            for col in range(1, row):
                # Each element is the sum of the two elements above it
                new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])

        # The last element of each row is '1'
        if row > 0:
            new_row.append(1)

        # Add the completed row to the triangle
        triangle.append(new_row)
    
    return triangle

# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
