# 호텔 예약 계산 프로그램
# 1박2일 성인 1인 기준 - 스탠다드 : 50000원, 슈페리어 : 70000, 디럭스 : 90000, 스위트룸 : 1000000
# 어린이(7세 미만)는 스탠다드 : 30000원, 슈페리어 : 50000, 디럭스 : 70000, 스위트룸 : 80000
# 지낼 날을  체크인 날짜와 체크 아웃를 입력 받고 날짜를 빼서 입력 받는다.
# 조식을 포함하시겠습니까? + 지낸 날*10000
# 공항버스를 이용하시겠습니까? 총 금액 + 인당 10000
# 예약자 이름으로 예약 받고(메모장에다가)
# 이름을 통해서 random으로 방 호수를 알려주는 예약확인!

from datetime import date
import random 

# 룸과 가격 리스트작성
rooms = ['스탠다드', '슈페리어', '디럭스', '스위트룸']
prices= [50000,70000,90000,100000]

# 체크인 체크아웃 날짜 계산
print('Hoseo 호텔에 오신 것을 환영합니다!!')

y = int(input('체크인 년도를 입력해 주세요 : '))
m = int(input('체크인 월을 입력해 주세요 : '))
d = int(input('체크인 일을 입력해 주세요 : '))
oy = int(input('체크아웃  년도를 입력해 주세요 : '))
om = int(input('체크아웃 월을 입력해 주세요 : '))
od = int(input('체크인 일을 입력해 주세요 : '))
check_in = date(y, m, d)
check_out = date(oy, om, od)
night = abs(check_in-check_out).days

# 룸, 사람 수, 나이, 조식, 공항버스 입력
room = input(str(rooms)+'중 방을 골라주세요.')      
people = int(input('사람 수를 적어주세요 : '))

ages = []
no_kid = 0
no_adult = 0

for k in range(people):
    ages.append(int(input('나이를 적어주세요 : ')))

for age in ages:
    if age < 7:
        no_kid = no_kid + 1
    else:
        no_adult = no_adult + 1
        
breakfast = str(input('조식을 포함하시겠습니까?(Y/N)'))
airbus = str(input('공항버스를 이용하시겠습니까?(Y/N)'))

# 입력한 수에 대한 총 금액계산
nadult = night * no_adult
nkid = night * no_kid
count = no_adult + no_kid

if room == '스탠다드' and breakfast == 'N'and airbus == 'N':
    print('총 금액은',str((prices[0]*nadult)+((prices[0]-20000)*nkid))+'원 입니다')
elif room == '스탠다드' and breakfast == 'N' and airbus == 'Y':
    print('총 금액은',str((prices[0]*nadult)+((prices[0]-20000)*nkid)+(count*10000))+'원 입니다')
elif room == '스탠다드' and breakfast == 'Y' and airbus == 'N':
    print('총 금액은',str((prices[0]*nadult)+((prices[0]-20000)*nkid)+(nadult*10000)+(nkid*10000))+'원 입니다')
elif room == '스탠다드' and breakfast == 'Y' and airbus == 'Y':
    print('총 금액은',str((prices[0]*nadult)+((prices[0]-20000)*nkid)+(nadult*10000)+(nkid*10000)+(count*10000))+'원 입니다')
elif room == '슈페리어' and breakfast == 'N' and airbus == 'N':
    print('총 금액은',str((prices[1]*nadult)+((prices[1]-20000)*nkid))+'원 입니다')
elif room == '슈페리어' and breakfast == 'N' and airbus == 'Y':
    print('총 금액은',str((prices[1]*nadult)+((prices[1]-20000)*nkid)+(count*10000))+'원 입니다')
elif room == '슈페리어' and breakfast == 'Y' and airbus == 'N':
    print('총 금액은',str((prices[1]*nadult)+((prices[1]-20000)*nkid)+(nadult*10000)+(nkid*10000))+'원 입니다')
elif room == '슈페리어' and breakfast == 'Y' and airbus == 'Y':
    print('총 금액은',str((prices[1]*nadult)+((prices[1]-20000)*nkid)+(nadult*10000)+(nkid*10000)+(count*10000))+'원 입니다')
elif room == '디럭스' and breakfast == 'N' and airbus == 'N':
    print('총 금액은',str((prices[2]*nadult)+((prices[2]-20000)*nkid))+'원 입니다')
elif room == '디럭스' and breakfast == 'N' and airbus == 'Y':
    print('총 금액은',str((prices[2]*nadult)+((prices[2]-20000)*nkid)+(count*10000))+'원 입니다')
elif room == '디럭스' and breakfast == 'Y' and airbus == 'N':
    print('총 금액은',str((prices[2]*nadult)+((prices[2]-20000)*nkid)+(nadult*10000)+(nkid*10000))+'원 입니다')
elif room == '디럭스' and breakfast == 'Y' and airbus == 'Y':
    print('총 금액은',str((prices[2]*nadult)+((prices[2]-20000)*nkid)+(nadult*10000)+(nkid*10000)+(count*10000))+'원 입니다')
elif room == '스위트룸' and breakfast == 'N' and airbus == 'N':
    print('총 금액은',str((prices[3]*nadult)+((prices[3]-20000)*nkid))+'원 입니다')
elif room == '스위트룸' and breakfast == 'N' and airbus == 'Y':
    print('총 금액은',str((prices[3]*nadult)+((prices[3]-20000)*nkid)+(count*10000))+'원 입니다')
elif room == '스위트룸' and breakfast == 'Y' and airbus == 'N':
    print('총 금액은',str((prices[3]*nadult)+((prices[3]-20000)*nkid)+(nadult*10000)+(nkid*10000))+'원 입니다')
elif room == '스위트룸' and breakfast == 'Y' and airbus == 'Y':
    print('총 금액은',str((prices[3]*nadult)+((prices[3]-20000)*nkid)+(nadult*10000)+(nkid*10000)+(count*10000))+'원 입니다')

# 예약자 이름 입력
fp = open('customer.txt','a')
reservation = input('예약자 이름을 적어주세요! : ')
print(reservation+'으로 예약 되었습니다.')
print(reservation, file = fp) # 파일에 예약자 백업
fp.close()

# 예약확인
room_num = [201,202,203,204,205,206,207,301,302,303,304,305,306,307]

cus = open('customer.txt','r')
temp = cus.readlines()
rese = []

for k in temp:
    rese.append(k.strip('\n'))
    
name = input('예약한 이름은? ')

# 방 호수가 반복되지 않게 나오려면?...
for n in range(1):
    if name == reservation :
        print(reservation+'님은',random.choice(room_num),'호로 예약되어있습니다.')
    else:
        print('예약자 이름에서 찾을 수 없습니다.')
cus.close()

