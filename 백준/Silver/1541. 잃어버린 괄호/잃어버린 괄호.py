import re
s = input()

arr = re.findall(r'\d+|\S',s)
arr = [str(int(i)) if i.isdigit() else i for i in arr]

arr[0] = '({}'.format(arr[0])

for i in range(len(arr)):
    if arr[i] == '-':
        arr[i] = ')-('
arr += [')']

result = ''.join(arr)
print(eval(result))