days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30,
'December':31}

# A. 알파벳 순 정렬
print(sorted(days.keys()))
print('-'*20)

# B. 일수 기준 정렬
print(sorted(days.items(), key=lambda x: x[1])) # 오름차순

# print(sorted(days.items(), key=lambda x: x[1], reverse=True)) # 내림차순

# C. 3자리 입력 처리
inp = input('2자리 월 이름을 입력하세요: ')

for k in days:
    if k[:2] == inp:
        print(days[k])
        break
