def matrix_to_list(i,e):
    result = [] # this will hold the full matrix

    for row in range(i,e+1):
        row_list = [] # holds one row

        for col in range(i,e+1):
            row_list.append(row * col)

        result.append(row_list)
    return result

print(matrix_to_list(1,4))
print()

