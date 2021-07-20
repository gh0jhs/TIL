# 1. N 까지의 총합

```python
# 정수 num을 기준으로, 1~num까지의 총 합을 구하는 함수를

# 1.for 문을 사용하여
# 2.while문을 사용하여
# 작성하시오.


#  for문만 사용하여 풀기
def sum_with_for(num):
    total = 0
    for i in range(1,num+1):
        total += i
    return total

# while문만 사용하여 풀기
def sum_with_while(num):
    cnt = 1
    total = 0
    while cnt<=num:
        total += cnt
        cnt += 1
    return total


# 아래 코드는 바꾸지 않습니다.
print(sum_with_for(4))    # 10
print(sum_with_while(4))  # 10
print(sum_with_for(5))    # 15
print(sum_with_while(5))  # 15
```



# 2. 리스트의 총곱

```python
# 사용자가 입력한 정수 num을 기준으로, 1~num으로 이루어진 리스트의 총 곱을 구하는 함수를

# 1.for문을 사용하여
# 2.while문을 사용하여
# 작성하시오.

# for문만 사용하여 풀기
def mul_with_for(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


# while문만 사용하여 풀기
def mul_with_while(numbers):
    i = 0
    total =1
    while True:
        total *= numbers[i]
        i+=1
        if i==len(numbers):
            break
    return total

# 아래 코드는 바꾸지 않습니다.
num = int(input('정수를 입력하세요'))
numbers = list(range(1, num+1))

# 아래 두코드 모두 in 4 => out 24 / in 5 => out 120 를 만족해야 합니다.
print(mul_with_for(numbers))
print(mul_with_while(numbers))
```

