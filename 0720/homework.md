# Homework

# 1. Mutable & Immutable

```python
#변경 가능한 것 : List, Set, Dictionary
#변경 불가능한 것 : String, Tuple, Range
```



# 2. 홀수만 담기

```python
list(range(1,51,2))
```



# 3. Dictionary 만들기

```python
dict_a = {'박진성':27, '홍길동':28, '김싸피':29}
```



# 4. 반복문으로 네모 출력

```python
n = 5
m = 9
cnt = 0
while cnt <m:
    print('*'*n)
    cnt += 1
```



# 5. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp>=37.5 else print('입실 가능')
```



# 6. 평균 구하기

```python
scores = [80, 89, 99, 83]
total = 0
for score in scores:
    total += score
print(total/len(scores))
```

