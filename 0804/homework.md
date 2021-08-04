# HomeWork

### Bootstrap

공식 문서의 Component를 활용하여 물음에 답하시오. 

1) 각 문항에 제시된 이미지는 현재 lab.ssafy.com에서 사용중인components이다. 제시된 요소에 사용된 Bootstrap Component가 무엇인지 작성하시오. 

2) 위에서 답한 Bootstrap Component를 사용하여 제시된 요소와 유사한 형태가 되도록 코드를 작성하시오.



### 1. Components

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  <title>Document</title>
</head>
<body>

  <div class="d-grid gap-2 col-6 mt-5 mx-auto">
    <button type="button" class="btn btn-success btn btn-primary">Sign in</button>
  </div>



  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script></body>
</body>
</html>
```



### 2. Components

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
    <button type="button" class="btn btn-dark"><img src="https://edu.ssafy.com/asset/images/logo.png"></button>
    <div class="btn-group" role="group">
      <button id="btnGroupDrop1" type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        프로젝트
      </button>
      <div class="btn-group" role="group">
        <button id="btnGroupDrop1" type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          그룹들
        </button>
    <button type="button" class="btn btn-dark">활동</button>
    <button type="button" class="btn btn-dark">마일스톤</button>
    <button type="button" class="btn btn-dark">스니펫</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script></body>
</body>
</html>
```



### 3. Components

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <ul class="nav nav-pills  ">
    <li class="nav-item">
      <a class="nav-link text-muted border border-secondary" href="#">Prev</a>
    </li>
    <li class="nav-item">
      <a class="nav-link active border border-secondary" aria-current="page" href="#">1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link border border-secondary text-dark" href="#">2</a>
    </li>
    <li class="nav-item">
      <a class="nav-link border border-secondary text-dark" href="#">3</a>
    </li>
    <li class="nav-item">
      <a class="nav-link border border-secondary text-dark" href="#">4</a>
    </li>
    <li class="nav-item">
      <a class="nav-link border border-secondary text-dark" href="#">Next</a>
    </li>
  </ul>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script></body>
</body>
</html>
```



### 4. Login Page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <form>
  </div>
  <div class="alert alert-danger" role="alert">
    Invalid Login or password.
  </div>
    <h1>SSAFY 전용 GitLab 시스템</h1>
    
    <h4 class="text-center">Sign in</h4>
    <hr>
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Username or email</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label">Password</label>
      <input type="password" class="form-control" id="exampleInputPassword1">
    </div>
    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1">
      <label class="form-check-label" for="exampleCheck1">Remember me</label>
    </div> 
      <a href="#" class="alert-link text-decoration-none ">Forgot your password?</a>
    </div>
    <div class="d-grid gap-2 col-6 mt-5 mx-auto">
      <button type="button" class="btn btn-success btn btn-primary">Sign in</button>
    </div>

  </form>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script></body>
</body>
</html>
```







