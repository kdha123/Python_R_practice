import codecs
import csv

# EUC-KR로 저장된 CSV 파일 읽기
filename = "test.csv"
fp = codecs.open(filename, "r", "euc-kr")

reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
