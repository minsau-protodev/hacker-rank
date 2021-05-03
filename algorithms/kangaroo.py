def kangaroo(x1, v1, x2, v2):
    # Write your code here
    start_diff = x1 - x2
    velocity_diff = v2 - v1
    if (v2 > v1 or velocity_diff == 0):
        return 'NO'
    if((start_diff % velocity_diff) == 0):
        return 'YES'
    else:
        return 'NO'


print(kangaroo(0, 2, 5, 3))
print(kangaroo(0, 3, 4, 2))
print(kangaroo(43, 2, 70, 2))
