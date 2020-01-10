# 구구단 처리를 하는데 시작 단수와 마지막 단수를 입력받아서
# 시작단수 부터 마지막 단수 사이의 모든 단수를 출력한다.
# range(시작, 끝 +1, 증감)
for i in range(1, 11, 2):
    print(i)
#     print(i, end="")

startNum = int(input(" 시작단수를 입력해주세요 : "))
endNum = int(input(" 마지막 단수를 입력해주세요 : "))

for i in range(1, 10):
    for j in range(startNum, endNum + 1):
        print(" %d X %d = %d " % (j, i, i*j), end="")
    print()
