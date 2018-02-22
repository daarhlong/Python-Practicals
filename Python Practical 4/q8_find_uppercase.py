def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    elif (str[0].isupper()) == 1:
        return 1 + find_num_uppercase(str[1:])
    else:
        return find_num_uppercase(str[1:])

print(find_num_uppercase('Good MorninG'))
