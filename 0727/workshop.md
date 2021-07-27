# 1. 무엇이 중복일까

```python
# 교수님께서 가르쳐주신 딕셔너리 활용을 해봤다
def duplicated_letters(word):
    lst=[]
    my_dict={}
    for key in word:
        my_dict[key] = my_dict.get(key, 0) + 1 ###
    for key in my_dict:
        if my_dict[key] > 1:
            lst.append(key)
    return lst

# 내가 푼 것
def duplicated_letters(word):
    lst = []
    for char in word:
        if word.count(char) > 1:
            lst.append(char)
    lst = set(lst) # 중복 제거
    lst = list(lst)
    return lst
```

```python
duplicated_letters('apple') #=> ['p']
duplicated_letters('banana') #=> ['a', 'n']

['p']
['a', 'n']
```





# 2. 소대소대

```python
def low_and_up(word):
    pass
    new_word =''
    cnt = 0
    for char in word:
        if cnt % 2 == 0:
            new_word += char.lower()
        else:
            new_word += char.upper()
        cnt += 1

    print(new_word)
    return new_word

low_and_up('apple') #=> aPpLe
low_and_up('banana') #=> bAnAnA
```





# 3. 숫자의 의미

```python
def lonely(numbers):
    result = [numbers[0]]
    for num in numbers:
        if result[-1] != num:
            result.append(num)
    print(result)
    return result

lonely([1, 1, 3, 3, 0, 1, 1]) #=>[1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) #=> [4, 3]
```

