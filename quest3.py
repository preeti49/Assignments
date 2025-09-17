def indexes_below_threshold(lst, threshold):
    result = []
    for i, num in enumerate(lst):
        if num < threshold:
            result.append(i)
    return result

print(indexes_below_threshold([2, 3, 5, 10, 9, 0],10))
