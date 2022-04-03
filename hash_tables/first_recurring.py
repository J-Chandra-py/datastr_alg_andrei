# Given an array = [2,5,1,2,3,5,1,2,4],
# Tell the first recurring character
# for the above array it should return 2
# For array = [2,3,4,5]
# It should return undefined

def first_recurring(arr):
    l = len(arr)
    # Create hash_table
    hash_dict = {}

    for i in arr:
        # Check for if the current is already present in dictionary
        # If present, return the recurring element
        # or else, add a key-value pair into the dictionary
        if i in hash_dict:
            return i
        else:
            hash_dict[i] = i
        # If there are no recurring elements, then return 'undefined' as message
        if i == l - 1:
            return 'undefined'


if None:
    print("check")

print(first_recurring([1,2,3,5,4,6,8,3,4,5,4,2,5,1,2,6,4]))
print(first_recurring([]))