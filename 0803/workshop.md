# 1. Semantic Tag

```css
/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.bg-white {
  background-color: white;
}
.bg-lightgrey {
  background-color: lightgrey;
}
/* 2. header, nav, footer 태그의 margin을 4px로 만들어주세요. */
.m-4 {
  margin: 4px;
}
/* 3. header, nav, footer 태그의 padding을 4px로 만들어주세요. */
.p-4 {
  padding: 4px;
}
/* 4. h1 태그를 수평 중앙 정렬 시켜주세요. */
.text-center {
  text-align: center;
}
/* 5. section 태그는 width 490px height 300px, 
   aside 태그는 width 280px height 300px로 만들어주세요.*/
.section-wh {
  width: 490px;
  height: 300px;
}
.aside-wh {
  width: 280px;
  height: 300px;
}
/* 6. 모든 semantic 태그의 border 두께를 1px, 실선, 검은색으로 만들어주세요. */
.border {
  /* 크기 스타일 색상 */
  border: 1px solid black;
}
/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */
.br-4 {
  border-radius: 4px;
}
```



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="bg-lightgrey m-4 p-4 border br-4">
    <h1 class="text-center">header</h1>
  </header>
  <nav class="bg-lightgrey m-4 p-4 border br-4">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="bg-lightgrey border br-4 section-wh">
      <h2>section</h2>
      <article class="bg-white border br-4">
        <h3>article1</h3>
      </article>
      <article class="bg-white border br-4">
        <h3>article2</h3>
      </article>
    </section>
    <aside class="bg-lightgrey border br-4 aside-wh">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="bg-lightgrey m-4 p-4 border br-4">
    <h2>footer</h2>
  </footer>
</body>
</html>

```

