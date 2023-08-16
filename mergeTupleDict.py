def merge_tuple_dict(*tuple_val, **dict_val):
    merged_dict = {}
    dict_values = list(dict_val.values())
    
    for key in tuple_val: 
        if dict_values:
            merged_dict[key] = dict_values.pop(0) # Assign the value to the key and remove it from the list
    
    return merged_dict

print(merge_tuple_dict('world', 'country', 'city', AS='South Asia', BD='Bangladesh'))

