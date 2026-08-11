# 함수 연습_1

# 1. 인사 함수
# hello() 함수를 만들어 "안녕하세요!"를 출력하세요.

def hello():
    print("안녕하세요!")

hello()

# 2. 이름 출력 함수
# 이름을 매개변수로 받아 "안녕하세요, ○○님!"을 출력하는 greet(name) 함수를 만들어보세요.

def greet(name):
    print("안녕하세요,", name, "님!")

greet("홍길동")

# 2번 수정 코드
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("tom")

# 3. 두 수의 합
# 두 정수를 매개변수로 받아 더한 값을 반환하는 add(a, b) 함수를 만들어보세요.

def add(a, b):
    return a + b

add(3, 5)

# 4. 두 수의 곱
# 두 수를 받아 곱한 값을 반환하는 multiply(a, b) 함수를 만들어보세요.

def multiply(a, b):
    return a * b

multiply(4, 7)

# 5. 홀수/짝수 판별
# 정수 하나를 받아 짝수면 "짝수", 홀수면 "홀수"를 반환하는 check_even_odd(num) 함수를 만들어보세요.

def check_even_odd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

check_even_odd(10)

# 6. 큰 수 찾기
# 두 수를 받아 더 큰 숫자를 반환하는 get_max(a, b) 함수를 만들어보세요.

def get_max(a, b):
    if a > b:
        return a
    else:
        return b

get_max(8, 20)

# 7. 세 수의 평균
# 세 개의 숫자를 받아 평균을 계산해서 반환하는 average(a, b, c) 함수를 만들어보세요.

def average(a, b, c):
    return (a + b + c) / 3

average(98, 78, 34)

# 8. 문자열 길이 구하기
# 문자열을 하나 받아 문자열의 길이를 반환하는 get_length(text) 함수를 만들어보세요.

def get_length(text):
    return len(text)

get_length("ArithmeticError")

# 9. 리스트의 합
# 숫자가 들어있는 리스트를 매개변수로 받아 모든 숫자의 합을 반환하는 list_sum(numbers) 함수를 만들어보세요.

def list_sum(numbers):
    return sum(numbers)

list_sum([3, 4, 5, 6])

# 9번 수정 코드
def list_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

print(list_sum([3, 4, 5, 6]))

# 10. 비밀번호 확인
# 비밀번호를 매개변수로 받아 "python123"과 같으면 "로그인 성공", 다르면 "비밀번호가 틀렸습니다"를 반환하는 check_password(password) 함수를 만들어보세요.

def check_password(password):
    if password == "python123":
        return "로그인 성공"
    else:
        return "비밀번호가 틀렸습니다."

check_password("python13")