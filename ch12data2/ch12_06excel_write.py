import openpyxl

# 엑셀 파일 열기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 활성화된 시트 추출하기 -> sheet1이 열려있으면 1을 불러오고 2열려있으면 2불러옴.
sheet = book.active

# 서울을 제외한 인구를 구해서 쓰기
# chr(i) -> 유니코드 코드 포인트가 정수 i 인 문자를 나타내는 문자열을 돌려줍니다. ex) chr(65) = A
for i in range(0, 9):
    a = str(chr(i + 66))
    total = int(sheet[a + "3"].value)
    seoul = int(sheet[a + "4"].value)
    output = total - seoul
    print("서울 제외 인구 = ", output)
    # 쓰기
    sheet[a + "21"] = output
    cell = sheet[a + "21"]

    # 폰트와 색상 변경해보기
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    # 왜 쓰는지 모르겠음
    cell.number_format = cell.number_format

# 엑셀 파일 저장하기
filename = "population.xlsx"
book.save(filename)
print("ok")
