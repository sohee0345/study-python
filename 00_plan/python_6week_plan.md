# 6주 Python 전체 계획표

## 전체 목표

| 주차 | 핵심 주제 | 주차 종료 목표 |
|---|---|---|
| 1주차 | Python 기초 | if / for / list / 함수 기본 문제 직접 해결 |
| 2주차 | Python 응용 + NumPy | Python 기초를 유지하며 배열/차원 이해 |
| 3주차 | Pandas | 조건 필터링, groupby, 결측치 등 직접 사용 |
| 4주차 | 데이터 전처리 | Feature/Target, Encoding, Scaling 흐름 이해 |
| 5주차 | 머신러닝 기본 | fit → predict → 평가 전체 흐름 이해 |
| 6주차 | 종합 실전 | 데이터부터 전처리/모델링까지 직접 연결 |

---

# 1주차 — Python 기초

## 핵심 내용

- 변수 / 자료형
- 연산자
- if / elif / else
- for
- while
- list
- tuple
- dictionary
- set
- 문자열
- 함수
- return

## 하루 문제 구성

```text
조건문       1문제
반복문       1문제
리스트/문자열 1문제
함수         1문제
종합         1문제
```

## 목표

다음 정도의 코드는 빈 화면에서 작성할 수 있어야 한다.

```python
numbers = [3, 7, 8, 12, 15, 20]

result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num)
```

그리고 함수로 변경할 수 있어야 한다.

```python
def get_even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result
```

### 토요일
Python 기초 테스트 10문제

### 일요일
틀린 문제 재풀이

---

# 2주차 — Python 응용 + NumPy

## Python

- 함수 반복 연습
- lambda
- map
- list comprehension
- try / except
- 중첩 반복문
- dictionary 응용

## NumPy

- np.array()
- ndim
- shape
- indexing
- slicing
- reshape
- axis
- sum
- mean
- max
- min

## 하루 문제 구성

```text
Python 기초       2문제
Python 응용       1문제
NumPy             3문제
```

## 목표

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

를 보고

```text
shape = (2, 3)
ndim = 2
```

를 바로 설명할 수 있다.

### 토요일
Python 5문제 + NumPy 5문제

---

# 3주차 — Pandas 집중

## 핵심 내용

- Series
- DataFrame
- head / info / describe
- 컬럼 선택
- 행 선택
- loc / iloc
- 조건 필터링
- sort_values
- value_counts
- map
- apply
- groupby
- isnull
- fillna
- drop
- merge

## 하루 문제 구성

```text
Python 기초    2문제
NumPy 복습     1문제
Pandas         4~5문제
```

## 필수 코드

```python
df[df["age"] >= 20]
```

```python
df.groupby("class")["score"].mean()
```

```python
df["age_group"] = df["age"].map(
    lambda x: (x // 10) * 10
)
```

```python
df.isnull().sum()
```

## 목표

간단한 데이터 분석 문제를 보면
어떤 Pandas 기능을 사용해야 하는지 떠오른다.

### 토요일
Python 3문제 + NumPy 2문제 + Pandas 7문제

---

# 4주차 — 데이터 전처리

## 핵심 내용

- Feature / Target
- train / test
- train_test_split
- 결측치 처리
- Numerical / Categorical Feature
- One-Hot Encoding
- Label Encoding
- StandardScaler
- MinMaxScaler
- fit
- transform
- fit_transform

## 하루 문제 구성

```text
Python/Pandas 복습  2문제
전처리 코드         3문제
개념 설명           2문제
```

## 필수 코드

```python
x = df.drop("survived", axis=1)
y = df["survived"]
```

```python
df["age"] = df["age"].fillna(df["age"].mean())
```

```python
scaler.fit_transform(x_train)
scaler.transform(x_test)
```

## 이해해야 할 질문

- 왜 Feature와 Target을 나누는가?
- 왜 Train/Test를 분리하는가?
- 왜 Encoding을 하는가?
- 왜 Scaling을 하는가?
- 왜 scaler를 Train 데이터에 fit 하는가?

### 토요일
전처리 종합 테스트

---

# 5주차 — 머신러닝 기본

## 전체 흐름

```text
데이터 로드
↓
EDA
↓
결측치 처리
↓
Feature / Target
↓
Train / Test
↓
Encoding
↓
Scaling
↓
모델 생성
↓
fit
↓
predict
↓
평가
```

## 핵심 내용

- Classification
- Regression
- fit
- predict
- accuracy
- 기본 평가 지표
- Model Parameter
- Hyperparameter
- Cross Validation

## 하루 문제 구성

```text
Python 기초        2문제
Pandas/전처리      2문제
ML                 3문제
```

## 목표

다음 코드를 보고 역할을 설명할 수 있다.

```python
model.fit(x_train, y_train)
pred = model.predict(x_test)
```

단순히 코드를 외우는 것이 아니라
전체 머신러닝 흐름 속에서 각 코드의 위치를 이해한다.

### 토요일
전처리 + 머신러닝 종합 테스트

---

# 6주차 — 종합 실전

## 핵심 목표

새로운 문법을 많이 배우기보다
기존 내용을 연결한다.

처음에는 다음 한 줄에서 시작한다.

```python
df = pd.read_csv("data.csv")
```

그 다음 직접 진행한다.

```text
데이터 구조 확인
↓
결측치 확인
↓
필요한 컬럼 선택
↓
데이터 전처리
↓
Feature / Target
↓
Train / Test
↓
Encoding
↓
Scaling
↓
Model
↓
fit
↓
predict
↓
평가
```

## 6주차 진행 방식

### 월
자료를 보면서 전체 과정 1회

### 화
일부 코드만 참고하여 전체 과정 1회

### 수
최대한 안 보고 작성

### 목
다른 데이터 또는 조건으로 다시 작성

### 금
약한 부분 집중 복습

### 토
최종 종합 테스트

### 일
6주 오답 / 취약 개념 정리

---

# 매일 공통 루틴

```text
1. 당일 수업 복습
2. Python 기초 문제 최소 2개
3. 현재 주차 핵심 문제
4. 전날 오답 1~2문제
```

---

# 권장 하루 시간

| 구분 | 시간 |
|---|---:|
| 수업 복습 | 30~40분 |
| 문제 풀이 | 40~50분 |
| 오답 | 20분 |
| 누적 복습 | 10~20분 |
| 총합 | 1시간 30분~2시간 |

---

# 주차별 비중 변화

```text
1주차
Python ██████████

2주차
Python ██████
NumPy  ██████

3주차
Python ███
NumPy  ██
Pandas ████████

4주차
Python ███
Pandas ████
전처리 ████████

5주차
Python ███
Pandas ███
전처리 ████
ML     ███████

6주차
전체 내용 종합
```
