# 1. Built-in 함수

```python
print()
sum()
max()
min()
input()
```



# 2. 정중앙 문자

```python
def get_middle_char(string):
    n = len(string)
    if n%2 == 1:
        return string[n//2]
    else:
        return string[n//2-1:(n//2+1)]


get_middle_char('ssafy')
get_middle_char('coding')
```



# 3. 위치 인자와 키워드 인자

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')

ssafy(location='대전', name='철수')

ssafy('영희', location='광주')

#4 ssafy(name='길동', '구미')

4번 오류
```



# 4. 나의 반환값은

```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3,7)

None이 나온다.
```



# 5. 가변 인자 리스트

```python
def my_avg(*args):
    total = 0
    for arg in args:
        total+= arg
    return total/len(args)

my_avg(77, 83, 95, 80, 70)

81.0
```

