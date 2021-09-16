# HomeWork

### 1. User Model BooleanField

```python
is_staff
is_active
is_superuser
```



### 2. username max length

```python
max_length=150
```



### 3. login validation

```python
is_authenticated
```



### 4. Login 기능 구현

```python
(a) AuthenticationForm
(b) login
(c) form.get_user()
```



### 5. who are you?

```python
Anonymoususer
```



### 6. 암호화 알고리즘

```python
Django uses the `PBKDF2` algorithm with a `SHA256` hash
```



### 7. Logout 기능 구현

```python
함수명 logout과 겹쳐서 재귀형식으로 작동해서 정상작동 불가능 스택오버플로우
함수명을 logout에서 바꾸거나 장고가 제공하는 logout의 이름을 as로 다른 이름으로 바꾸어주어 해결해준다.
```

