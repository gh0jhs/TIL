# Workshop

# 1. 간단한 N의 약수

```python
N = int(input())
for i in range(1,N+1):
    if N%i == 0:
        print(i, end=' ')
```



# 2. 중간값 찾기

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
numbers.sort()
print(numbers)
middle = len(numbers)//2 + 1
print(numbers[middle-1])
```



# 3. 계단 만들기

```python
number = int(input())
for i in range(1,number+1):
    for k in range (1,i+1):
        print(k, end =' ')
    print('')
```

