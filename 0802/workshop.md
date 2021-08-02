# 1. img tag

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
  <img src="../image/my_photo.png" alt="">
</body>
</html>
```



# 2. 파일 경로

```
(a)../image/my_photo.png
(b)C:\Users\Jinseong\Desktop\ssafy2\image\my_photo.png
```



# 3. Hyper Link

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
  <a href="https://ssafy.com"><img src="../image/my_photo.png" alt=""></a>
</body>
</html>
```



# 4. 선택자

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
  #ssafy > p:nth-child(2){
    color: red;
  }
  </style>
</head>
<body>
  <div id="ssafy">
    <h2>어떻게 선택 될까?</h2> 
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>


</body>
</html>
```

1) 첫 번째 단락

2)두 번째 단락

3)nth-child(2)는 부모의 모든 자식 중에서 2번째 이므로 어떻게 선택될까?가 1이고 2인 첫번째 단락이 색깔이 변했고 nth-of-type(2)는 p태그만 카운트하여 두번째 단락이 색깔이 변했다.