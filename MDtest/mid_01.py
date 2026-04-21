str = 'Hello, IoT'

# A. 3번 반복
print(str * 3)

# B. 처음 4문자
print(str[:4])

# C. 마지막 5문자
print(str[-5:])

# D. 소문자
print(str.lower())
# 대문자
print(str.upper())


# E. 역순
print(str[::-1])


# 문자열[start:end:step]
# 처음 4글자	s[:4]	Hello, IoT → Hell
# 처음 n글자	s[:n]	s[:3] → 앞 3글자
# 마지막 5글자	s[-5:]	Hello, IoT → , IoT
# 마지막 n글자	s[-n:]	s[-4:] → 뒤 4글자
# 전체 문자열	s[:]	원래 문자열 그대로
# 역순 출력	s[::-1]	Hello → olleH
# 2칸씩 출력	s[::2]	짝수 인덱스만
# 1칸씩 출력	s[::1]	전체 그대로
# 뒤에서 2칸씩	s[::-2]	거꾸로 2칸 간격
# 중간 일부만	s[2:6]	인덱스 2~5까지