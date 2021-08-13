import sys
sys.stdin = open('input.txt')

def itoa():

    n = int(input())
    result = ''
    isMinus = False
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while n!=0:
        for i in lst:
            if n < 0:
                isMinus = True
                n *= -1
            elif int(i) == n%10 :
                n = n//10
                result = i + result
    if isMinus == True:
        result = '-' + result
    print(result)

itoa()
itoa()
itoa()
itoa()
itoa()
itoa()