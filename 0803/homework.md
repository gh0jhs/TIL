# 1. Semantic Tag

```
header, section, footer
```



# 2. input Tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="https://search.naver.com">
    <div>
      <label for="username">USERNAME : </label>
      <input type="text", placeholder="아이디를 입력해 주세요.", id="username", name="username">
    </div>
    <div>
      <label for="pwd">PWD : </label>
      <input type="password", id="pwd", name="pwd">
      <input type="submit", value="로그인">
    </div>
  </form>
</body>
</html>
```



# 3. 크기 단위

```
rem
```



# 4. 선택자

```html
  <style>
    /* 자손 결합자 */
    div p {
      color: crimson;
    }

    /* 자식 결합자 */
    div > p {
      color: blue;
    }
  </style>

/* 자손결합자 div p 는 div아래에 모든 p에 대해서 적용하고 자식결합자 div > p는 div아래 바로 2칸 인덴테이션되있는 자식들 p 에게만 적용한다. */
```

