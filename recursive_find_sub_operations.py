from doing_the_math import doing_the_math

def find_sub_operations(operation):
    list_of_open = []
    index = -1
    while index+1<len(operation):
        index+=1
        char = operation[index]
        if char == "(":
            list_of_open.append(index)
        elif char == ")":
            operation[list_of_open[-1]:index+1] = doing_the_math(operation[list_of_open[-1]+1:index])
            index = list_of_open[-1]
            list_of_open.pop()

    return operation