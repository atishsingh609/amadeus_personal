
def delete_middle_element_stack(stack, count, len):

    if count == int(len/2):
        stack.pop()
        return
    top_element = stack.pop()
    delete_middle_element_stack(stack, count+1, len)
    stack.append(top_element)


def call_fun():
    stack = [1,2,3,4,5,6,7,8]
    delete_middle_element_stack(stack, 0, len(stack))
    return stack

print(call_fun())


