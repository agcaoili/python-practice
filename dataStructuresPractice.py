# Practice using stacks by writing function that can assess validity of bracket input
def valid_brackets(str):
    bracket_key = {"(":")",
                   "[":"]",
                   "{":"}"}
    stack = []
    list1 = list(str)
    for item in list1:
        if item in bracket_key:
            stack += item
        else:
            if item == bracket_key[stack[-1]]:
                stack.pop()
            else:
                return False
    return stack == []

print(valid_brackets("({}[])"))


