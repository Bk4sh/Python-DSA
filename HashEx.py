def item_in_common1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 2, 5]
list2 = [3, 5, 6]
print(item_in_common1(list1, list2))
print(item_in_common2(list1, list2))