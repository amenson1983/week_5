if _name_ == '__main__':
    user_dict = get_dict_from_file('user.json')
    for i in range(len(user_dict['hobbies'])):
        print('User"s', i+1, 'hobby is: ', user_dict['hobbies'][i])
    count = 0
    for i in range(len(user_dict['children'])):
        count += i
    print('The number of user"s children: ', count+1)

    elder = user_dict['children'][0]
    for child in user_dict['children']:
        if child['age'] > elder['age']:
            elder = child
    print('The name of the elder child is: ', elder['firstName'])

    user_dict['email'] = 'jane@company.com'
    print(user_dict)