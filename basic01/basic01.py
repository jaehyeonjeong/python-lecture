print("hello python")
# python의 주석 방법
# crtl + / 를 사용하면 맞춰서 주석 하긴함
num01 = 10
num02 = 3.14
print(num01,num02)
print(num01)
print(num02)
name = "장성호"
age =20
print(name,age)
print("age : " , age)
print("age : " +str(age)) #숫자를 문자로 바꿔주는 함수 str()
print(f"age : {age}") #요즘 많이 쓰는 방식 {}안에 변수를 넣어서 사용함 fstring
print(f"age : {age} , name : {name}")
print("age : {} , name : {}".format(age,name)) # 이것은 예전 방식으로 {} 안에 format()을 사용해서 맵핑시킴
print("age : {0} , name : {1}".format(age,name)) # 이것도 예전 방식
print("age : %d , name : %s" %(age,name)) # 이것도 예전 방식
a = 10
b = 5
print(f"{a}+{b}={a+b}")
pi = 3.14159
print(f"pi={pi:.2f}")
hour = 9
minutes = 8
print(f"현재시간 - {hour:02d}:{minutes:02d}")
money = 15000
print(f"현재 가진 현금 : {money:,}원")