string = input()
stack = []

def findHead(stack):
    return stack[-1] if len(stack) else  None

def pop(stack, s):
    head = findHead(stack)
    global num
    num = None

    if isinstance(head, int):
        num = stack.pop()
        head = findHead(stack)

    if head == "(" and s == ")":
        stack.pop()
        stack.append(2)
    elif head == "[" and s == "]":
        stack.pop()
        stack.append(3)

    head = findHead(stack)

    if isinstance(head, int) and num:
        stack.append(stack.pop() * num)

for s in string:
    if s == "(" or s == "[":
        stack.append(s)
    elif len(stack):
        pop(stack, s)
        
        if len(stack) > 1 and isinstance (stack[-1], int) and isinstance(stack[-2], int):
            stack.append(stack.pop() + stack.pop())
    else:
        stack.append(s)

if len(stack) == 1 and isinstance(stack[0], int):
    print(stack.pop())
else:
    print(0)