# Python_01_wrokshop

## 1. 세로로 출력하기

```python
number = int(input())
for i in range(number) :
    print(i+1)
```

## 2. 거꾸로 세로로 출력하기

```python
number = int(input())
for i in range(number,-1,-1) :
    print(i)
```

## 3. N줄 덧셈 (SWEA #2025)

```python
number = int(input())
total = 0
for i in range (1,number+1) :
    total += i
print(total)
```

