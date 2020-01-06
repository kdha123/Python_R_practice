#ctrl + enter 실행하기
#ctrl + l 화면지우기
a <- 3
b <- 5
a+b
 
a = 10
a = 'hi python'
a = "hi!"
a = hi 
ls() #변수목록
rm(list=ls()) #변수삭제

#r  패키지
dim(available.packages())
installed.packages()

# r 패키지 설치와 제거
install.packages("ggplot2") #설치만 되고 메모리에 올라간 것은 아님
library(ggplot2) # library로 준비를 시켜줘야함.
search() #메모리에 로딩된 패키지
remove.packages("ggplot2") #패키지 제거

# r 에서 제공하는 데이터
data()
iris
cars 

# 간단한 입출력
getwd() #workspace를 보여줌
##setwd('d:/study/') 디렉토리를 설정함
##저장하기
write.table(iris,'iris.csv')
write.table(iris,'iris2.csv',row.names = F)
write.table(iris,'iris3.csv',row.names = F,quote = F)

##읽어오기
s <- read.table('s.csv', header = T, sep = ',')
help("read.table")
s <- read.csv('s.csv')
s

##클립보드에서 가져오기
s<-read.table(file = 'clipboard', header = T)
s

#변수명: 문자, 숫자, -, _, . 사용가능, 첫글자는 영문자, 대소문자구분, 한글가능

name<- '홍길동'
age <- 20
hobby <- '달리기'
is1004<-T
#데이터형
mode(name)
mode(age)
mode(hobby)
mode(is1004)
#데이터 구조
class(name)
class(age)
class(hobby)
class(is1004)
