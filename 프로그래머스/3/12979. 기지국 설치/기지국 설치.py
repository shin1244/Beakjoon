def solution(n, stations, w):
    elt_list = []
    result = 0
    www = (w*2+1)
    while stations:
        station = stations.pop(0)
        elt = [station - w, station + w]
        if elt_list and elt[0] < elt_list[-1][-1]:
            elt_list[-1][-1] = elt[-1]
        else:
            elt_list.append(elt)
    idx = 0
    while elt_list:
        elt = elt_list.pop(0)
        diff = elt[0] - idx - 1
        result += diff // www + (1 if diff % www != 0 else 0)
        idx = elt[-1]
    if idx < n:
        diff = n-idx
        result += diff // www + (1 if diff % www != 0 else 0)
    return result