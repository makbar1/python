a= 11
b = 5
c =50

conditions = [
    a > 10,
    b < 4,
    c > 30
]

# If all conditions are met i.e AND for all
if all(conditions):
    print('Wow')
# If any of the conditions are met i.e OR
if any(conditions):
    print("Super Wow")
