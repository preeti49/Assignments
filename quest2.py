def check_list(lst):

    if len(set(lst)) != 5:
        return False
    

    for i in range(1, len(lst)):
        if lst[i] == lst[-1]:
            return False
        
    return True
print(check_list([1, 3, 2, 4, 5, 5, 8]))    





