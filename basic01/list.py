#변수명 = 값

num01 = 10
num02 = 3.14
num03 = 0o17 #8진수
num04 = 0x1A #16진수
print (num01, num02, num03, num04)
print (num01 + num02)
print (num01 - num02)
print (num01 * num02)
print (num01 ** num02)
print (num01 **3 ) #거듭제곱
print (num01 / num02)
print (num01 % 3) #나머지
print (num01 // 3) #몫

str01 = """hello python""" # 리스트로 관리
print(str01 + "!!!") 
print(str01 * 3) # 문자열에 곱하기 연산 가능
print(str01[0] + str01[1],str01[2], str01[3], str01[4]) #인덱싱 + 는 문자열 공백없이 연결, , 는 공백으로 구분
print(str01[0:5]) # 슬라이싱
print(str01[2:5]) # 슬라이싱
print(str01[0:]) # 슬라이싱
print(str01[:7]) # 슬라이싱
print(str01[0:10:2]) # 슬라이싱 2칸씩 건너뛰기 [시작:끝:간격]
print(str01[::-2]) # 슬라이싱 2칸씩 건너뛰기 [시작:끝:간격]
print("I hate pthon".replace("hate","love")) # 문자열 바꾸기
print("I {0} {1}".format("hate", "python")) # 문자열 바꾸기
print("I {emotion} {language}".format(emotion="hate", language="python")) # 문자열 바꾸기
emotion = "love"
print(f"I {emotion} python") # f스트링 , 파이썬 3.6 이상에서 사용가능
a = 3
b = 5
print(f"{a} + {b} = {a+b}") # f스트링 나머지는 문자에서 처리 가능
print(f"{'hi':<10}!!") # 왼쪽정렬 오른쪽으로 10칸 확보
print(f"!!{'hi':>10}") # 오른쪽정렬 왼쪽으로 10칸 확보
print(f"!!{'hi':^10}!!") # 가운데정렬 양쪽으로 10칸 확보
print(f"!!{'hi':=>10}!!") # 오른쪽정렬 왼쪽은 =로 채우기
print(f"!!{'hi':=<10}!!") # 왼쪽정렬 오른쪽은 =로 채우기``
print(f"!!{'hi':=^10}!!") # 가운데정렬 양쪽은 =로 채우기
print(f"!!{1500000:,}") # 천단위 콤마 찍기 - 자동 처리 인가 보네... 넣으면 3자리 마다 , 찍어줌