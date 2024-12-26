def reverse_string(string):

    stack = []
    for i in string:
        stack.append(i)
    reverse_lst = []
    while stack:
        reverse_lst.append(stack.pop())
    return "".join(reverse_lst)


print("reverse_string", reverse_string("abcdef"))