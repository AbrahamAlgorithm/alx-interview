def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for m in range(1, i):
            row.append(triangle[i-1][m-1] + triangle[i-1][m])
        row.append(1)
        triangle.append(row)

    return triangle
