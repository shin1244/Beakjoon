n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

resultW = 0
resultB = 0

def Beakjoon(arr):
    global resultW
    global resultB
    if arr[0][0] == 0:
        for row in arr:
            for col in row:
                if col != 0:
                    mid_row = len(arr) // 2
                    mid_col = len(arr[0]) // 2
                    Beakjoon(slice_2d(arr, 0, mid_row, 0, mid_col))        # 왼쪽 위
                    Beakjoon(slice_2d(arr, mid_row, len(arr), 0, mid_col))  # 왼쪽 아래
                    Beakjoon(slice_2d(arr, 0, mid_row, mid_col, len(arr[0])))  # 오른쪽 위
                    Beakjoon(slice_2d(arr, mid_row, len(arr), mid_col, len(arr[0])))  # 오른쪽 아래
                    return
        resultW += 1
        return

    elif arr[0][0] == 1:
        for row in arr:
            for col in row: 
                if col != 1:
                    mid_row = len(arr) // 2
                    mid_col = len(arr[0]) // 2
                    Beakjoon(slice_2d(arr, 0, mid_row, 0, mid_col))        # 왼쪽 위
                    Beakjoon(slice_2d(arr, mid_row, len(arr), 0, mid_col))  # 왼쪽 아래
                    Beakjoon(slice_2d(arr, 0, mid_row, mid_col, len(arr[0])))  # 오른쪽 위
                    Beakjoon(slice_2d(arr, mid_row, len(arr), mid_col, len(arr[0])))  # 오른쪽 아래
                    return
        resultB += 1
        return



    


def slice_2d(arr, row_start, row_end, col_start, col_end):
    sliced_array = [row[col_start:col_end] for row in arr[row_start:row_end]]
    return sliced_array


Beakjoon(arr)

print(resultW)
print(resultB)
