shopping_list = ['노트북','아이폰xs','가방'] # 리스트 변수 선언 및 할당
shopping_list.append('시계') #리스트 맨 뒤에 추가 # 리스트 원소(값) 추가
shopping_list.insert(1,'시계')
print(shopping_list)
#shopping_list[2] = '아이폰xr' #리스트 원소 수정

#삭제는 3가지 방법이 있음
#shopping_list.remove('아이폰xr') # remove 메서드는 삭제하려고 하는 원소가 여러개 있을 때
shopping_list.append('시계')      #맨 처음에 찾는 원소만 하나 삭제한다.

#shopping_list.pop() # 리스트 맨 마지막 원소만 삭제

#shopping_list.pop(-2) # 리스트 맨 마지막 원소 앞의 원소  삭제
#shopping_list.pop(2) # 리스트 앞에서 2번째 삭제
del shopping_list[1]
print(shopping_list)

#오름차순 정렬(ㄱ,ㄴ,ㄷ, 순)
shopping_list.sort()


#내름차순 정렬(ㅎ~ㄱ 순)
shopping_list.sort(reverse=True)
print(shopping_list)
