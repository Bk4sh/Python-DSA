def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    min_index = int(len(my_list)/2)
    left = merge_sort(my_list[:min_index])
    right = merge_sort(my_list[min_index:])
    return merge(left, right)

print(merge([1,3,8,7], [2,4,6,5]))
print(merge_sort([4,2,1,5,3,6,8,7]))