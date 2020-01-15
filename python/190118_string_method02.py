tax = ['990102-1234567','980505-2233123']
new_tax = []
tax.append('000311-4211234')
tax.append('001111-3333333')


for h in tax : # 0번째 위치 문자열
    new_tax.append(h[:8]+'******')
print(new_tax)




'''
for h in range(len(tax)): # h는 0부터 tax리스트의 길이 앞까지 반복
    new_tax.append(tax[h][:8]+'******')
print(new_tax)
'''



'''
for human in tax:
    if human[7] == '1' or human[7] == '3':
        print('남자')
    else :
        print('여자')
'''
