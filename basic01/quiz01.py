# 1. " Python Developer " 문자열에서 앞뒤 공백을 제거하여 출력하세요.
str01 = " Python Developer "
print(str01.strip())
# 2. "hello WORLD" 를 모두 대문자로 변환하여 출력하세요.
str02 = "hello WORLD"
print(str02.upper())
# 3. "hello WORLD" 를 모두 소문자로 변환하여 출력하세요.
str03 = "hello WORLD"
print(str03.lower())
# 4. "python programming" 문장에서 "programming"을 "algorithm"으로 변경하여 출력하세요.
str04 = "python programming"
print(str04.replace("programming","algorithm"))
# 5. "Data-Engineer" 에서 "-" 를 "_" 로 변경해 출력하세요.
str05 = "Data-Engineer"
print(str05.replace("-","_"))
# 6. "Busan Harbor" 가 "Busan" 으로 시작하는지 검사하여 출력하세요.
str06 = "Busan Harbor"
print(str06.startswith("Busan"))
# 7. "cloud-service.org" 가 ".org" 로 끝나는지 검사하여 출력하세요.
str07 = "cloud-service.org"
print(str07.endswith(".org"))
# 8. "JavaToPython" 문자열에 "Python"이 포함되어 있는지 True/False로 출력하세요.
str08 = "JavaToPython"
print("Python" in str08)
# 9. "security_patch_v5" 문자열에서 "patch" 의 시작 위치 인덱스를 출력하세요.
# index() 나 find() 나 똑같다
str09 = "security_patch_v5"
print(str09.index("patch"))
# 10. "DeepLearning" 문자열 길이를 출력하세요.
str10 = "DeepLearning"
print(len(str10))
# 11. "API_ERROR_404" 에서 "ERROR" 를 "error" 로 변경해 출력하세요.
str11 = "API_ERROR_404"
print(str11.replace("ERROR","error"))
# 12. " Tokyo Night View" 문자열에서 왼쪽 공백만 제거해 출력하세요.
str12 = " Tokyo Night View"
print(str12.lstrip())
# 13. "Seoul " 문자열에서 오른쪽 공백만 제거해 출력하세요.
str13 = "Seoul "
print(str13.rstrip())
# 14. "FastAPI" 를 폭 12, 가운데 정렬로 출력하세요.
str14 = "FastAPI"
print(f"{str14:^12}")
# 15. "debug_mode" 에서 "mode" 를 "LEVEL" 로 변경해 출력하세요.
str15 = "debug_mode"
print(str15.replace("mode","LEVEL"))
# 16. "Python3.12.1" 에서 . 을 제거한 뒤 영문/숫자만 남았는지 검사하여 출력하세요.
str16 = "Python3.12.1"
print((str16.replace(".","")).isalnum())
# 17. "Pyramid" 문자열을 뒤집어서 출력하세요.
str17 = "Pyramid"
print(str17[::-1])
# 18. "Hello\nPython" 에서 줄바꿈 \n 을 공백 " "으로 변경해 출력하세요.
str18 = "Hello\nPython"
print(str18.replace("\n"," "))
# 19. "alphaNUM123" 의 대소문자를 서로 반대로 변경해 출력하세요.
str19 = "alphaNUM123"
print(str19.swapcase())
# 20. "Google Search Console" 을 타이틀 케이스로 변환하여 출력하세요.
str20 = "google search console"
print(str20.title())
# 21. "password=1234;" 에서 = 의 인덱스 위치를 출력하세요.
str21 = "password=1234;"
print(str21.index("="))
# 22. "http://localhost" 가 "https" 로 시작하는지 검사하여 출력하세요.
str22 = "http://localhost"
print(str22.startswith("https"))
# 23. "__init__method" 에서 "method" 의 시작 인덱스를 출력하세요.
str23 = "__init__method"
print(str23.index("method"))
# 24. "CamelCASEstring" 이 영문/숫자만으로 구성되어 있는지 검사하여 출력하세요.
str24 = "CamelCASEstring"
print(str24.isalnum())
# 25. "ErrorWarningCritical" 에서 "Warning" 시작 인덱스를 출력하세요.
str25 = "ErrorWarningCritical"
print(str25.index("Warning"))
# 26. "Python_SCRIPT" 에서 "_" 뒤 문자열만 소문자로 출력하세요.
str26 = "Python_SCRIPT"
print(str26[:str26.find("_")+1] + str26[str26.find("_")+1:].lower())
# 27. "MachoCulture" 에서 "Culture" 를 "CULTURE" 로 변경해 출력하세요.
str27 = "MachoCulture"
print(str27[0:5] + str27[5:].upper())
# 28. "EncodingTest" 에서 "Test" 가 처음 나오는 인덱스를 출력하세요.
str28 = "EncodingTest"
print(str28.index("Test"))
# 29. 문자열을 입력받아 "start" 로 시작하면 "yes", 아니면 "no" 출력하세요.
str29 = input("문자열을 입력하세요")
print("yes" if str29.startswith("start") else "no")
# Python의 if문 작성방법은 들여쓰기 방식이다 .
# yml과 비슷하다 보면 될듯
if str29.startswith("start") :
 print("yes")
else :
 print("no")
# 삼항연산자 = 조건 ? True : False 파이썬에 없음
# 만약 쓰고 싶다면 ?
# print("yes" if str29.startswith("start") else "no")
# 이렇게 쓰면 됨 ㅇ_ㅇ;;