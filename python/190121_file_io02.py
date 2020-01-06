fp = open('hoseo.txt','r')

# readlines매서드를 이용해
# 줄단위로 리스트 원소에 삽입
temp = fp.readlines()
text = []

print(temp)
for k in temp:
    text.append(k.strip('\n'))

print(text)
for line in text:
    print(line)

fp.close()
