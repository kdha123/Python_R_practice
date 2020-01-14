# dictionary -> {key:value[,key : value]} -> js : json 형식
# key 값을 중복해서 쓰면 덮어쓰기가 된다.
dic1 = {1: 'a', 2: 'b', 3: 'c', 3: 'e'}
print(dic1, type(dic1))

# 학생 딕셔너리 생성
student = {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과'}
print(student, type(student))

# 학생의 이름 데이터 가져오기
print(student['이름'])
print(student.get('이름'))

# 모든 키를 출력
# 순수한 list 가 아니면 처리가 잘 안될 수 있다.
keyList = list(student.keys())
print(keyList)

valueList = student.values()
print(valueList)

# 학생딕셔너리가 가지고 있는 모든 데이터 출력해보기
for a in keyList:
    print(a, ":", student[a])

print(student.items())
studentList = list(student.items())
print(studentList)
studentList.append(('연락처', '010-1111-1111'))
print(studentList)
print(studentList.pop())
print(studentList)

# 딕셔너리의 데이터 추가
singer = {}
singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'TT'

# 같은 키를 사용해서 데이터를 넣으면 수정이 된다.
singer['구성원 수'] = 10
print(singer)

# singer 딕셔너리의 대표곡 항목을 삭제
del singer['대표곡']

print(singer)

