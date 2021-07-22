# 1. 회문 판별

```python
# while

def is_pal_while(word):
    length = len(word)
    cnt = -1
    new_word = ''
    while True:
        new_word += word[cnt]
        cnt -=1
        if -cnt == length+1:
            break

    if word == new_word:
        return True
    else:
        return False


# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
```

