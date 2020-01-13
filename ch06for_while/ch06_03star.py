# for 문을 이용한 별마름모 출력
# print('\u2605')
for s in range(1, 6):
    for k in range(5-s, 0, -1):
        print(" ", end="")
    for i in range(1, s*2):
        print('\u2605', end="")
    print()
for a in range(6, 2, -1):
    for m in range(a-6, 1, 1):
        print(" ", end='')
    for j in range(1, (a*2)-4):
        print("\u2605", end='')
    print()

# 예시
totalRow = 10
inc = 1
# blankcnt -> 4,3,2,1,0,1,2,3,4
# totalRow // 2 -> 4 ==> range(1, totalRow // 2+1, 2)
blankcnt, starcnt, multi = 4, 1, 1
for i in range(1, totalRow):
    blankcnt = (totalRow // 2 - i) * multi
    # print(blankcnt)
    # 빈 공간을 출력
    for j in range(1, blankcnt+1):
        print(" ", end="")
    # 별 출력
    for k in range(1, starcnt + 1):
        print('\u2605', end="")
    print()
    # 별을 최대치를 출력하면 공백은 증가(+값)해야하고 별의 갯수 감소(-값)
    if i == totalRow // 2:
        multi = multi * -1

    starcnt += 2 * multi
