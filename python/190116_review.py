# 16일 수업 리뷰

# and, or
print(1 and 0)
print(1 and 1)
print(True and False)
print(True and True)
print(1 or 0)
print(1 or 1)
print(True or False)
print(True or True)

# 조건문
height = 131
weight = 99

if height>=130 and weight <100 :
    print('탑승하세요')
else :
    print('죄송합니다')



# 리스트
heros = ['아이언맨','캡틴아메리카','헐크']
print(heros)
print(heros[1]) # 리스트 인덱싱

#리스트 추가/삽입
#heros.append('호크아이') 리스트 맨 뒤에 추가
heros.insert(2,'호크아이') # 리스트 사이에 추가
print(heros[-1]) # 리스트 맨 마지막 원소값 출력
heros.append('베놈')
print(heros)

#리스트의 원소 삭제 3가지 방법
#heros.pop() 특정 위치의 원소 삭제할 수 있음
#heros.remove('베놈')
#del heros[-1]
print(heros)

# 베놈을 블랙위도우로 리스트 원소 값 수정
heros[-1] = '블랙위도우'
print(heros)

#리스트 정렬
heros.append('그린고블린')
heros.sort(reverse=True) # 사전 내림차순 정렬
print(heros)

# 출력함수
print("호서대")
print('호서대')

# + 연산자
print('31'+'23') # 문자열 결합
print(31+23) # 산술연산
#print('31'+23) # 에러 :  문자열과 숫자형에 + 연산 불가

# * 연산자
print('데굴' * 3) # 문자열과 정수간의 곱셈 연산은 문자열을 반복해서 출력한다.
print(9 * 3)
#print('데굴' *'3') # 에러 : 문자열 간의 곱셈은 불허

# 기타 연산
print(5 / 2) # 나누기
print(5 // 2) # 몫
print(5 % 2) # 나머지 연산
print(2 ** 8) # 거듭제곱
# 입력함수
n = input('이릅을 입력 : ')
print('안녕',n)

# 숫자를 문자로, 문자를 숫자로
print(str(1) + '2')
print(1 + int('2'))

# 리스트
heros
