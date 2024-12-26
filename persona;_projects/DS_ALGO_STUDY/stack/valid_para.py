def valid_para(expression):
    par_dict = {"[": "]", "{": "}", "(": ")"}
    stack = []
    for par in expression:
        if par in par_dict.keys():
            stack.append(par)
        else:
            if len(stack) > 0 and par_dict[stack[-1]] != par:
                return False
            else:
                stack.pop()

    return len(stack) == 0

print(valid_para("{}"))

