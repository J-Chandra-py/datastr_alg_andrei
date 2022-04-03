# MergeSortedArrays([0, 3, 4, 31], [4, 6, 30])
# A would be [0, 3, 4, 4, 6, 30, 31]

def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merge_list = []

    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1

    # Started from comparing the smallest elements of
    # The both lists, and appended the smallest element
    # Consecutively increment of positional parameter
    # for the array from which element is appended.
    while i+j <= (len(arr1) + len(arr2) - 2):
        print(arr1[i], arr2[j])
        if arr1[i] < arr2[j]:
            merge_list.append(arr1[i])
            i += 1
        else:
            merge_list.append(arr2[j])
            j += 1
            if j == len(arr2):
                merge_list.append(arr1[i])

    # if arr1[i] > arr2[j]:
    #     merge_list.append(arr1[i])
    # else:
    #     merge_list.append(arr2[j])
    return merge_list


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
