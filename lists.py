def remove_elements(list_to_remove_elements):
    new_list = list_to_remove_elements[:]
    for index in sorted([0,4,5], reverse=True): #para que los indices no cambien cuando vaya borrando
        if index < len(new_list):
            del new_list[index]
    return new_list
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def add_elements(list_to_add_elements):
   new_list= list(list_to_add_elements)
   new_list.insert(0, 'Pink')
   new_list.append('Yellow')
   return new_list
print(add_elements(['Red', 'Green', 'White', 'Black']))

def is_empty(list_to_check):
   if len(list_to_check) is 0:
       return True
   else:
       return False
print(is_empty([]))

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False
print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'],['Red', 'Green', 'White', 'Black', 'Pink']))

def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify) != 3:
        return 'error'
    else:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
        return list_of_lists_to_modify
    
print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
