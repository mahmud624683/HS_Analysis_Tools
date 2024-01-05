def modify_dict(my_dict):
    dict1 = my_dict
    my_dict = 2

    print(my_dict)
    print(dict1)
    
original_dict = 0
modify_dict(original_dict)
print(original_dict)  # Output: {'key': 'new_value', 'new_key': 'new_item'}