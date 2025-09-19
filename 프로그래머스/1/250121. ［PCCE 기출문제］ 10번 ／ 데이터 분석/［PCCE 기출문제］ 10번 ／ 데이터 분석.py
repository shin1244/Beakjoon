def solution(data, ext, val_ext, sort_by):
    target = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    result = []

    for d in data:
        if d[target[ext]] < val_ext:
            result.append(d)
    result.sort(key=lambda x: x[target[sort_by]])

    return result