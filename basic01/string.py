name = "장성호"
print(name)
name = '성장호'
print(name)
name="""호장성"""
print(name)
say = """Life is short,
You need python"""
print(say)
say = """Life's is short,\r\nYou need python""" # 큰따옴표안에 작은 따옴표는 가능하다
print(say)
print("="*50)
print("author : jjang051")
print("="*50)
print(len(say))
print(say[0])
print(say[1])
print(say[2])
print(say[2-1])
print(say[-0]) # 아무의미 없음
print(say[-1]) # 음수는 -1부터 의미를 가지게 됨
print(say[0:4]) # 0에서 4번째 문자열까지 출력
print(say[0:-4]) # 뒤에서 4번째 문자열을 빼고 출력
print(say[0:]) # :의 뒤를 비워두면 끝까지
dateStr = "20251201Rainy" #날짜와 날씨 뽑아보기
print(f"날짜 : {dateStr[0:8]} , 날씨 : {dateStr[8:]}")
# str은 불변객체임
# ex) dateStr[1] = "f" -> 불변객체기에 오류터짐
print(f"{'hi':>10}") # 부등호의 방향의 따라 앞으로 뒤로 공백이 결정됨
print(f"{'hi':^10}") #10글자의 가운데 정렬
print(f"{'hi':-^20}") #20자를 만드는데 나머지를 - 로 채우고 가운데 정렬
print(f"{7:0>8}") # 숫자로도 가능 (문자열 취급되서 그런가??)
print(f"{1234567:>12,}") # 앞이 비워지면서 자릿수를 맞추고 ,로 구분까지 해줌
print(say.count('s')) # count는 특정 글자의 빈도 수를 집계함 , 대소문자를 구분함
print(say.count('X')) # 0이라고 출력하면 없음을 일컬음

#find() 해당하는 문자의 index 없으면 -1을 리턴함
print("say.find('b')",say.find("b"))


#index() 해당하는 문자의 index를 반환함 없으면 오류
print("say.index('s')",say.index("s"))

#join() '문자'.join(문자열) -> 해당하는 문자열 사이사이에 문자를 삽입한다
print("','.join(say)",','.join(say)) # ,로 문자열을 다 쪼개서 구분 지음
str01 = "   hi   "
print(str01.lstrip()) #좌공백제거
print(str01.rstrip()) #우공백제거
print(str01.strip()) #좌우공백제거

#replace() 바꿔치기
str02 = "Life is too short"
print(str02.replace("Life","Your leg"))

#isalpha() , isdigit() , isalnum() , isspace()
str03 = "Life"
print("str03.isalpha()",str03.isalpha()) # 순수한 문자만 있으면 True , 공백,특수문자,숫자가 들어가면 False 출력
str04 = "12345"
print("str04.isdigit()",str04.isdigit()) # 순수한 숫자만 있으면 True , 공백,특수문자,문자가 들어가면 False 출력
str05 = "Python3"
print("str05.isalnum()",str05.isalnum()) # 문자 숫자만 있으면 True , 공백,특수문자 들어가면 False 출력 
str06 = "     "
print("str06.isspace()", str06.isspace()) # 공백만 있으면 True , 특수문자,숫자,문자가 들어가면 False 출력
str07 = "life is too short"

#lower() , upper() , capitalize() , title()
print("str07.lower()",str07.lower()) # 모두 소문자로 변환
print("str07.upper()",str07.upper()) # 모두 대문자로 변환
print("str07.capitalize()",str07.capitalize()) # 문자열의 첫 글자만 대문자로 변환
print("str07.title()",str07.title()) # 공백 뒤 문자는 대문자로 변환

a=10
b=5
a,b = b,a # 변수의 값을 서로 바꾸는 방법 , temp라는 변수를 새로 만들어서 새로운 변곡점을 만들지 않고도 변수값을 바꾸기가 가능함
print(a,"===",b) # 5와 10 출력
