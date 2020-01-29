import openpyxl

# 엑셀 파일 읽기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append([row[0].value,
                 row[9].value])

# 필요없는 줄(헤더, 연도, 계) 제거하기
del data[0:3]

# 데이터를 인구 순서로 정렬합니다.
# key 가 첫번째 리스트 순서가 x이고 그 안에서의 두번째 x[1]이 키가 되서 정렬된다.
data = sorted(data, key=lambda x: x[1])

# print(enumerate(data))
# 하위 5위를 출력합니다.
for i, a in enumerate(data):
    if i >= 5:
        break
    print(i + 1, a[0], int(a[1]))

