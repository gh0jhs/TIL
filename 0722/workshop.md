# 1. 숫자의 의미

```python
def get_secret_word(lst):
    result = ''
    for i in lst:
        result += chr(i)
    print(result)
    return result


get_secret_word([83, 115, 65, 102, 89]) #=> 'SsAfY'
```



# 2. 내 이름은 몇일까?

```python
def get_secret_number(string):
    result = 0
    for i in string:
        result += ord(i)
    print(result)
    return result

get_secret_number('tom') #=> 336
```



# 3. 강한 이름

```python
def get_strong_word(string1, string2):
    result1 = 0
    result2 = 0
    # 각각 스트링 숫자 합 구하기
    for i in string1:
        result1 += ord(i)
    for i in string2:
        result2 += ord(i)
    # 숫자 합 결과 비교하기
    if result1 > result2:
        print(string1)
        return string1
    else :
        print(string2)
        return string2


get_strong_word('z', 'a') #/=> 'z'
get_strong_word('tom', 'john') #=> 'john
```

