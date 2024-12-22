line1 = [(8, 10), (4, 18), (2, 6), (16, 2), (8, 4), (9, 10), (14, 10), (18, 13)]
line2 = [(3, 20), (16, 8), (8, 6), (6, 1), (5, 9), (15, 13), (12, 16), (9, 16)]

def sum_x_coordinates(coords):
    total_sum = sum(x for x, y in coords)
    return total_sum

total_x_line1 = sum_x_coordinates(line1)

print(f"The total sum for x-coordinates in line 1 is {total_x_line1}")


