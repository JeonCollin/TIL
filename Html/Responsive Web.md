## Grid system
- 반응형 디자인의 웹페이지를 적절하게 표현
- 12개의 column: 약수가 많아서 유연하게 설계 가능

## 기본요소
- Container: column을 담는 공간
- Column: 실제 컨텐츠를 포함하는 부분
- Gutter: col 사이의 간격(x축은 padding, y축과 x축 제일 바깥은 margin으로 여백 생성)

## Tip
- class ="container": 적당하게 양 쪽에 margin을 준다
- container - row - col이 한 세트

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  /* <!-- 기본 형태 --> */
  <h2 class="text-center">Basic</h2>
  <div class="container">
    <div class="row">
      /* <!-- 그냥 col col col 하면 알아서 4칸씩 배정해 줌 --> */
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
    </div>
    /* <!-- 이렇게 명시적으로 4칸으로 설정해 주는게 더 좋다 --> */
    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
    </div>
    /* <!-- 상황에 따라 유연하게 설정할 수 있다. -->
     <!-- 12칸보다 넘치면 다음 행으로 넘어가버린다 --> */
    <div class="row">
      <div class="col-2">
        <div class="box">col-2</div>
      </div>
      <div class="col-8">
        <div class="box">col-8</div>
      </div>
      <div class="col-5">
        <div class="box">col-5</div>
      </div>
    </div>
  </div>

  <hr>
  /* <!-- Nesting -->
  <!-- col 안에 또 col로 나눈다 -->
  <!-- 일단 몇 칸씩 가져갈 건지 선언한다 --> */
  <h2 class="text-center">Nesting</h2>
  <div class="container">
    <div class="row">
      /* <!-- 우선 4칸을 가져간다 --> */
      <div class="col-4 box">
        <div>col-4</div>
      </div>
      /* <!-- 그 다음 남아있는 8칸을 가져간다 --> */
      <div class="col-8 box">
        <div class="row">
          /* <!-- 8칸을 또 12 칸으로 나눠서 6칸 씩 가져간다 -->
           <!-- 근데 24개니까 2번의 행으로 자동으로 분리된다 --> */
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <hr>
  /* <!-- Offset -->
  <!-- col 간에 원하는 만큼 간격을 준다 --> */
  <h2 class="text-center">Offset</h2>
  <div class="container">
    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      /* <!-- 가운데 4칸을 간격을 주기 위해 오프셋을 준다 -->
       <!-- col-n offset-m: m칸을 건너뛰어서 n칸을 차지해라 --> */
      <div class="col-4 offset-4">
        <div class="box">col-4 offset-4</div>
      </div>
    </div>
    <div class="row">
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <div class="box">col-6 offset-3</div>
      </div>
    </div>
  </div>

  <hr>
  /* <!-- Gutters -->
  <!-- padding, margin을 조절하여 간격을 설정한다 --> */
  <h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    /* <!-- gutter는 row에서 조절한다 --> */
    /* <!-- gx: x방향으로 padding 조절 --> */
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container ">
    /* <!-- gy: y방향으로 margin 조절 --> */
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Gutters(g-5)</h2>
  <div class="container">
    /* <!-- g: x, y를 모두 조절한다 --> */
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>
```

# Responsive web
- 웹 페이지를 다양한 화면 크기에서 적절하게 배치
- 6개의 break point
- 너비(width) 기준: xs, sm, md, lg, xl, xxl
- break point마다 **설정된 너비 값 이상**으로 화면이 커지면 gird system이 변한다
```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <!-- Breakpoints 기본 -->
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <!-- sm 사이즈 이상이면 col-6으로 적용된다 -->
      <!-- 그래서 크기가 커지면 한 줄에 2개의 col이 존재 -->
      <!-- md 사이즈 이상이면 2,8,2,12로 적용된다 -->
      <!-- lg 사이즈 이상이면 3,3,3,3으로 적용된다 -->
      <!-- xl 사이즈 이상이면 4,4,4,12로 적용된다 -->
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <hr>

  <!-- Breakpoints + Offset -->
  <!-- 사이즈는 항상 중간에 들어간다 -->
  <h2 class="text-center">Breakpoints + offset</h2>
  <div class="container">
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <!-- offset-특정사이즈-크기 -->
      <!-- 특정 사이즈 이상에는 모두 적용되므로 주의하자 -->
      <!-- 그 사이즈를 넘어가면 offset을 해제하자 -->
      <div class="col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>
```

