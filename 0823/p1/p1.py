T = int(input())
A = '+-*/()'
B = '+-*/'
for tc in range(1, T+1):
    word = input()
    stack = []
    top = -1
    result = ''
    for i in word:
        if i not in A:
            result += i
        else:
           if i == '(':
               stack.append(i)
               top += 1
           elif i == '+':
               if stack[top] in B:
                   result += '+'
               else:
                   stack.append(i)
                   top += 1
           elif i == '-':
               if stack[top] in B:
                   result += '-'
               else:
                   stack.append(i)
                   top += 1
           elif i == '*':
               if stack[top] == '*' or stack[top] == '/':
                   result += '*'
               else:
                   stack.append(i)
                   top += 1
           elif i == '/':
               if stack[top] == '*' or stack[top] == '/':
                   result += '/'
               else:
                   stack.append(i)
                   top += 1
           elif i == ')':
               while stack[top] != '(':
                   result += stack.pop()
                   top -= 1
print(result)