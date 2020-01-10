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
    for j in range(1, a*2-4):
        print("\u2605", end='')
    print()
