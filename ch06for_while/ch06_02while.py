# 1 ~ 10 까지 출력

i = 1
while i < 11:
    print(i)
    i += 1

# 1부터 숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가서 출력
i = 1
sum = 0
while True:
    sum += i
    i += 1
    if sum > 100:
        break
print(sum, i)

# 1 ~ 10 출력 홀수만 출력
# 첫번째 방법 : 1부터 시작하면서 2씩 증가
for i in range(1, 11, 2):
    print(i)
# 짝수인 경우 출력하지않고 반복처리를 계속할 수 있도록 한다.
i = 0
while i < 11:
    i += 1
    if i % 2 == 0:
        continue
    # 만약에 짝수면 출력하지 않는다.
    print(i)

