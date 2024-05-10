def remove_elements(list_to_remove_elements):
   if len(list_to_remove_elements) >=6:
       del list_to_remove_elements[5]
   if len (list_to_remove_elements) >=5:
       del list_to_remove_elements[4]
       del list_to_remove_elements[0]
   return list_to_remove_elements
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    b=len( list_to_add_elements)+1
    list_to_add_elements.insert(b,"Yellow")
    return list_to_add_elements
print(add_elements(['Red', 'Green', 'White', 'Black']))


def is_empty(list_to_check):
    return "ANSWER HERE"  # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    return "ANSWER HERE"  # Remove this line and implement


def list_of_lists(list_of_lists_to_modify):
    return "ANSWER HERE"  # Remove this line and implement
