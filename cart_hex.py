coordinates = [
    (8, 10), (4, 18), (2, 6), (16, 2), (9, 10), (14, 10), (18, 13), (3, 20), 
    (6, 1), (5, 9), (15, 13), (12, 16), (20, 16), (17, 13), (0, 4), (11, 12), 
    (10, 20), (13, 16), (19, 11), (1, 14), (7, 8)
]

for x, y in coordinates:
    product = x * y
    hex_product = hex(product)
    #print(f"({x}, {y}): {hex_product}")
    print(x*y,end="")