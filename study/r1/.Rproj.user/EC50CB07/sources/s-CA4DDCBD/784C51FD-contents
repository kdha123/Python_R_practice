install.packages('stringr')
library(stringr)
search()

# 문자열추출 str_extract('문자열','정규식')
s <- '김길동50둘리10희동이5'
str_extract(s,'[0-9]')
str_extract_all(s,'[0-9]')
str_extract_all(s,'[0-9]{1,3}')
str_extract_all(s,'[가-힣]{1,5}')
str_extract_all(s,'[^0-9]{1,3}')

# 문자열위치
str_locate(s,'둘리')
str_sub(s,4,str_length(s)-2)
s<-'Apple,Lemon'
str_to_lower(s)
str_to_upper(s)
str_replace(s,'e','이')
str_replace_all(s,'e','이')
help("str_replace_all")
str_c(s,'강가딘20')

# 문자열의 길이
str_length(s)

person <- c('둘리10', '김길동50', '희동이3')
person
s2 <- paste(person,collapse = "-") # 합치기
s2
str_split(s2,'-') # 자르기
# 데이터 입출력-------------
n <- scan() 
n
# help(scan) 쓰다가 모르면 help() 
c <- scan(what = character())
c

# vector, matrix, array, dataframe

# 벡터----------------
v1 <- c(1,2,3,4,5)
v1
V1 <- c(1:10)
V1
v1 <- seq(1,10,3)
v1 <- c(1:10)
v1
union(v1,V1) # 합집합
intersect(v1,V1) # 교집합
setdiff(v1,V1) # v1 - V1

sum(v1)
min(v1)
max(v1)
mean(v1)

name <- c('홍길동', '코난', '엘사','크리스토퍼')
gender <- c('남','남','여','남')
age <- c(10,8,50,16)

# factor : 범주형 데이터, 지정된 값을 가짐
fgender <- as.factor(gender) # 범주형 변수
fgender
mode(fgender)
class(fgender)
sum(fgender) # 계산이 되지 않는다. 수치형이지만

# 날짜데이터
d <- '2020-01-07'
mode(d)
d1 <-as.Date(d)
d1
mode(d1)
class(d1)
d2 <- c('20-01-07','20-01-03')
d3 <- as.Date(d2, '%y-%m-%d') #%y: 년도 2자리, %Y: 년도 4자리
d3 <- as.Date(d2, '%Y-%m-%d')
d3

#matrix --------------
m1 <- matrix(c(1:12), 2, byrow = T)
m1<- matrix(c(1:12), 5)
m1
m1[2:4,2] #[행,열]

#apply 함수적용
apply(m1, 1, max) # 행방향
apply(m1, 2, min) # 열방향
apply(m1, 2, mean)

# 사용자정의함수
f1<-function(x){
  x+c(100,200,300,400,500)
}
apply(m1, 2, f1)

# Array--------------
# 동일한 데이터를 가지는 다차원배열
a1<- array(c(1:24),c(3,4,2))
a1
# list : 키와 값이 한쌍으로 저장
a1 <- list('홍길동','달리기',10)
a1
a2 <- list(c(1:5),c('one','two','three'),TRUE)
a2
a3 <- list(no = c(1:5),name = c('one','two','three'),etc = TRUE)
a3$no
a3$name
a3$etcb 
a3$name[2]
#원소제거
a3$name <- NULL
a3


# 데이터프레임:2차원, 다른 데이터 유형을 가질 수 있다.
df <- data.frame()
df <- edit(df)
df
# 1)vector를 이용한 생성
no <- c(1:3)
name <- c("김","이","박")
pay <- c(200,210,220)
df1 <- data.frame(no,name,pay)
df1
mode(df1)
class(df1)
str(df1)
ncol(df1)
nrow(df1)
df1[c(2:3)]
summary(df1)
#subset(데이터프레임, 조건)조건에 맞는 데이터 추출
df2 <- subset(df1,pay>200)
df2
df2 <- subset(df1,pay<=200 | pay>=220)
df2
df2 <- subset(df1,pay>200 & pay<220)
df2
#------연습하기------
df <- data.frame(name=c('사과','딸기','수박'),price=c(1800,1500,3000),sales=c(24,38,13), pass=c(T,T,F))
df
mean(df$price)
mean(df$sales)
summary(df)
View(df)

library(ggplot2)
View(mpg)
mpg$manufacturer
summary(mpg)
qplot(data = mpg, x = hwy) # data에 mpg, x축에 hwy 변수 지정해 그래프 생성
# x축 cty
qplot(data = mpg, x=cty)
# x축 cty, y축 hwy
qplot(data = mpg, x=cty, y = hwy)
# x축 cty, y축 hwy, 선그래프 형태
qplot(data = mpg, x=cty, y = hwy, geom = 'line')
# x축 cty, y축 hwy, 상자 그림 형태
qplot(data = mpg, x=cty, y = hwy, geom = 'boxplot')
# x축 cty, y축 hwy, 상자 그림 형태 , drv별 색 표현
qplot(data = mpg, x=cty, y = hwy, geom = 'boxplot', colour = drv)


#오라클 연동