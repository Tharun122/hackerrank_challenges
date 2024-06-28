# Rotate 2d arrays
def print_2d_arr(arr):
    for i in range(len(arr)):
        temp = ""
        for j in range(len(arr[i])):
            temp += str(arr[i][j]) + " "
        print(temp)
    print("\n")

def rotate_2d_by_90(arr):
    m = len(arr)
    n = len(arr[0])
    output = []
    print_2d_arr(arr)
    for i in range(n):
        row = []
        for j in range(m):
            row.append(arr[j][n-i-1])
        output.append(row)
    print_2d_arr(output)
    return output


rotate_2d_by_90([[1,2,3,4],[4,5,6,6],[7,8,9,9]])
