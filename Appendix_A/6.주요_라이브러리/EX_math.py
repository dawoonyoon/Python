import math

print(math.factorial(5))

print(math.sqrt(7))

print(math.gcd(21, 14))

print(math.pi)

print(math.e)


"""
2차원 리스트(행렬)를 90도 회전하는 메서드
"""

def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length -1 - r] = a[r][c]

    return res

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(rotate_a_matrix_by_90_degree(a))