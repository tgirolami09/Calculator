#Should find the operations recursively not with a while loop.
#Then might be easier to deal with - sign all alone
from parse_operation import parse_operation as po
from recursive_find_sub_operations import find_sub_operations as fso
print(*fso(po(list(input("Give me the operation : ").replace(" ","")))))