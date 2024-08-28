import numpy as np

def solution(board, skill):
    board = np.array(board)
    board_shape = np.shape(board)
    temp = np.zeros((board_shape[0]+1, board_shape[1]+1))
    for arr in skill:
        if arr[0] == 1:
            temp[arr[1]:arr[3]+1, arr[2]] -= arr[-1]
            temp[arr[1]:arr[3]+1, arr[4]+1] += arr[-1]
        else:
            temp[arr[1]:arr[3]+1, arr[2]] += arr[-1]
            temp[arr[1]:arr[3]+1, arr[4]+1] -= arr[-1]
    
    for i in range(1, board_shape[1]):
        temp[:, i] += temp[:, i-1]
    
    temp = temp[:-1, :-1]
    return int(np.sum(board + temp >= 1))