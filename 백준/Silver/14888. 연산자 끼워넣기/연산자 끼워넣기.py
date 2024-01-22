n = int(input())
num_arr = list(map(int, input().split(' ')))
add, sub, mul, div = list(map(int, input().split(' ')))

minResult = 1e9
maxResult = -1e9

def dfs(num, index, add, sub, mul, div):
    global minResult, maxResult
    if index == n:
        minResult = min(num,minResult)
        maxResult = max(num,maxResult)
        return
    if add > 0:
        dfs(num+num_arr[index], index+1, add-1, sub, mul,div)
    if sub > 0:
        dfs(num-num_arr[index], index+1, add, sub-1, mul,div)
    if mul > 0:
        dfs(num*num_arr[index], index+1, add, sub, mul-1,div)
    if div > 0:
        dfs(int(num/num_arr[index]), index+1, add, sub, mul,div-1)
    

dfs(num_arr[0],1,add,sub,mul,div)
print(maxResult)
print(minResult)