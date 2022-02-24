def hourglasses(arr, i, j):
    return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i + 2][j:j+3])

def hourglassSum(arr):
    values = [hourglasses(arr, i, j) for i in range(0, 4) for j in range (0, 4)]
    return max(values)
