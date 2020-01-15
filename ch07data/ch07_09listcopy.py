# 별개의 새로운 리스트를 만든다. 예전에 데이터를 그대로 사용
oldList = ['짜장면', '탕수육', '군만두']
newList = oldList[:]
# newList = oldList.copy()
# for 문으로도 가능함.
print("oldList : ", oldList)
print("newList : ", newList)

oldList.append('탕수육')
print("oldList : ", oldList)
print("newList : ", newList)

oldList.remove('탕수육')
print(oldList)