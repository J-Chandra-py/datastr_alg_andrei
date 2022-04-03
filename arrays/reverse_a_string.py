# Create a functionn that reverse a string:
# 'Hi My name is Jayachandra' should be
# 'ardnahcayaJ si eman yM iH'

def reverse(string):
    # Check string
    if (not string) or (len(string) == 0) or not isinstance(string, str):
        return "pass a valid string"

    # list reverse and then use ''.join(arr)
    # arr = list(string)  #O(n)
    # arr.reverse()   #O(n)

    # extended slicing
    # string = string[::-1]

    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
print(reverse('Hi My name is Jayachandra'))
# print(''.join(lst))


# a = 'd'
# if a:
#     print('hi')