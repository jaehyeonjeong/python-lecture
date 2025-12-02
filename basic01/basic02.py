a=3
b=4
print(a+b) # 덧셈
print(a-b) # 뺄셈
print(a*b) # 곱셉
print(a/b) # 나눗셈 a를 b로 나눈 식 소숫점까지 포함함
print(a%b) # 나머지를 구하는 식
print(a**b) # 제곱의 표시 ex) a의 b제곱
print(7//3) # 7을 3으로 나눈 몫을 가져가라
print("hello"*5) # python은 반복 출력을 원할 경우 문자열에 곱셉기호를 사용해서 반복출력이 가능하다
a=0o177 # 8진수 표시 8진수는 7이 끝임 8보다 큰 숫자는 안들어감 o = 옥타의 줄임
print(a) # 1*8*8 + 7*8 + 7
b=0xabc # 10*16*16 + 11*16 + 12 Hexadecimal
print(b)
print(type(b)) # 타입을 보고 싶다면 사용하는 함수
print(type("hello"))
print(type(3.14))
print(type(True)) # True False 는 첫글자를 대문자로 써야함
name = input("이름을 입력하세요 : ")
print(name)
age = int(input("나이를 입력하세요 : "))
#print(name+"/"+(age + 10)) # input은 무조건 문자로 들어옴 처리할려면 int 함수를 써야함
print(f"{name} / {age + 10}")