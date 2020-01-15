'''
score = [[3.73, 3.90], [3.57, 4.01], [3.73, 3.90],[3.57, 4.01]]
y = 1
s = 1
for year in score:   
    s = 1
    for sm in year:
        print(y,'학년',s,'학기',sm)
        s = s + 1
    y = y + 1   


score = [[3.73, 3.90], [3.57, 4.01], [3.73, 3.90],[3.57, 4.01]]

for year in range(0,4): #학년은 1학년부터 4학년 까지
    for s in range(0,2): #학기는 1학기부터 2학기 까지
        print(year+1,'학년',s+1,'학기',score[year][s])

    
for dan in range(2,10):
#print('---------------')
    for x in range(1,10):
        print(dan,'*',x,'=',dan * x)
     print('-----------')

     
print('1학년 1학기',score[0])
print('1학년 2학기',score[1])
print('2학년 1학기',score[2])
print('2학년 2학기',score[3])
'''

