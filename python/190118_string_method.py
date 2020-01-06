# 문자열 메서드

profile = '박원민 학생은 산업심리학과에 재학 중 입니다. 이제 3학년 입니다.'

print(profile[1]+profile[2])
print(profile[-1])

#profile[0] = '김' # 에러  : 문자열 역시 튜플처럼 이뮤터블 자료형이다.

temp = list(profile)
temp[0] = '김
#profile = str(temp) #리스트 전체를 문자열로 바꿀 수 없다.

# 문자열 메서드 join을 사용해서 리스트의 원소를 하나의 문자열로 치환
profile =''.join(temp)
print(profile)



#for word in profile: # in뒤에는 range, 리스트, 문자열이 올 수 있다(순서를 가진다)
    #print(word)
