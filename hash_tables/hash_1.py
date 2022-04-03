def func():
    return 'ahhhhh!'

user = {
    'age' : 54,
    'name' : 'sally',
    'magic' : True,
    'scream' :  func,
}

user['age']
user['spell'] = 'abra kadabra'  #O(1)

print(user)
print(user['scream']()) #O(1)