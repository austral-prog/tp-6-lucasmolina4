def remove_elements(list_to_remove_elements):
   if len(list_to_remove_elements) >=6:
       del list_to_remove_elements[5]
   if len (list_to_remove_elements) >=5:
       del list_to_remove_elements[4]
       del list_to_remove_elements[0]
   return list_to_remove_elements

   

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    b=len( list_to_add_elements)+1
    list_to_add_elements.insert(b,"Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
   if len(list_to_check) == 0:
      return True
   else:
       return False


def check_lists(list_to_compare1, list_to_compare2):
   if len(list_to_compare1) >=3 and len(list_to_compare2)>=3:
       if list_to_compare1[2] == list_to_compare2[2]:
           return True
       else:
           False
   else:
       False


def list_of_lists(list_of_lists_to_modify):
    a = list_of_lists_to_modify[0][0:2]
    b = list_of_lists_to_modify[1][1:4]
    c = list_of_lists_to_modify[2][-2:]
    list_of_lists_to_modify = [a,b,c]
    return list_of_lists_to_modify
