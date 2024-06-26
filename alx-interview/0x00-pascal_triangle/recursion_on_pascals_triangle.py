def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the given number of rows.

    :param num_rows: The number of rows to generate.
    :return: A list of lists, where each inner list represents a row in Pascal's Triangle.
    """

    # Base Cases:
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    
    # Recursive Case:    
    else:
        # Call generate_pascals_triangle recursively with num_rows - 1.
        triangle = generate_pascals_triangle(num_rows - 1)
        # Get the last row of the previously generated triangle.
        last_row = triangle[-1]
        # Create a new row by starting and ending with 1 and computing the inner elements as the sum of the two elements above from the last row.
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle
    
# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
