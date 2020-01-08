# read.table()
# getwd()
f <- read.table('table.txt')
f

f <- read.table('table1.txt', header = T)
f
class(f) # data.frame
mode(f) # list
str(f) # 데이터 구성
f <- read.table('table1.txt', header = T, stringsAsFactors = F) # factor를 string으로
str(f)
f <- read.table('table2.txt', header = T, stringsAsFactors = F, sep = ",") # 구분기호를 ","로
f
f <- read.table(file = 'clipboard') # 클립보드에 있는 것
f
f <- read.table(file.choose(),header = T) # 파일 선택
f
f <- read.csv('table2.txt', header = T)
f

# 엑셀 파일을 위한 패키지를 설치해야함.
install.packages('xlsx')
library(xlsx)
f <- read.xlsx('s.xlsx',sheetIndex=1, encoding = 'UTF-8', header = T)
f
f <- read.xlsx('s.xlsx',sheetIndex=2, encoding = 'UTF-8', header = T)
f

# 변수명 지정
names(f)<- c('번호','이름','나이')
f

#write.table()
data()
cars
write.table(cars,'cars1.txt')
write.table(cars,'cars2.txt',row.names = F,quote = F)
write.table(cars,'cars3.txt',row.names = F,quote = F, sep = ",")
write.csv(cars,'cars.csv',row.names = F,quote = F)
write.xlsx(cars,'cars.xlsx',row.names = F)

#---------------
a<-5
print(a)
a
print('a=',a)
cat('a =',a) # cat을 이용해야함.
#--------------
v1 <- c(100,200,300)
mode(v1)
sum(v1)
summary(v1)
fruit <- c('딸기','체리','샤인머스캣')
fruit
mode(fruit)
#is.xxxx(), as.xxxxx()
f1 <- as.factor(fruit)
f1
sum(f1)
str(f1)
as.numeric(f1)
as.character(f1)

f2 <- as.factor(fruit, levels=c("샤인머스캣","딸기","체리")) # 형변환할 때 사용하는 것이기 때문에 오류발생
f2 <- factor(fruit, levels=c("샤인머스캣","딸기","체리"))
f2

#------------------
result <- c('수','우','미','양','가')
result
f1<- as.factor(result)
f1
f2 <- factor(result, ordered = T)
f2
f3 <- factor(result, ordered = T, levels = c('가','양','미','우','수')) # 순서가 존재하는 경우
f3
#------------------
# 숫자데이터 factor로 지정하기
v1 <- c(100,90,80,100,80,80)
f1 <- as.factor(v1)
f1
as.numeric(f1)
as.character(f1)

#-----------데이터 프레임
iris
str(iris)
head(iris,10)
tail(iris,5)
iris[3,]
iris[3,5]
iris[c(3,5),2]
head(iris[,c('Petal.Length','Species')])
head(iris$Species)
iris$Petal.Length[c(3,5)]
summary(iris$Sepal.Length)
sum(iris$Sepal.Length)
mean(iris$Sepal.Length)
median(iris$Sepal.Length)
quantile(iris$Sepal.Length) # 4분위수

# subset(데이터프레임, 조건)
subset(iris,Sepal.Width > 4 & Sepal.Length > 5)
subset(iris,Sepal.Width > 4 & Sepal.Length > 5, c('Sepal.Length','Sepal.Width','Species'))
iris$Sepal.Width > 4
iris$Sepal.Width > 4 & iris$Sepal.Length > 5
iris[3,]
# boolean 추출
iris[iris$Sepal.Width >4,]
iris[iris$Sepal.Width >4,c(T,F,F,F,T)]

f <- read.xlsx('s.xlsx',sheetIndex=1, encoding = 'UTF-8', header = T)
names(f) <- c('번호','이름','나이')
f
subset(f,나이 >=10, c('이름','나이'))
f[f$나이>=10,c(2,3)]
f[f$나이>=10,c('이름','나이')]
f$나이>=10
f[c(T,T,T),c(F,T,T)]

install.packages('sqldf')
library(sqldf)
longley
sqldf('select "GNP.deflator", GNP, Unemployed from longley where GNP > 300')

#연도별 GNP의 합을 출력
sqldf('select Year,sum(GNP) from longley group by Year')

#---------
f
save(f,file = 'ex1.rda')
load('ex1.rda')
f
dim(f)

library(ggplot2)
mpg
mpg <- data.frame(ggplot2::mpg)

install.packages('dplyr')
library(dplyr)
f<- rename(f,age=나이)
f
f$total <- f$age + f$번호
f
f$result <- ifelse(f$total >14,'good','normal')
f$result2 <- ifelse(f$total >14, 'good',ifelse(f$total>12,'normal','bad'))
f
iris %>% filter(Sepal.Length > 5)
iris %>% filter(Sepal.Length > 5 & Sepal.Width <4)
iris2<-iris %>%
  filter(Sepal.Length > 5 & Sepal.Width <4) %>%
  select(Sepal.Length, Sepal.Width, Species)
iris2$total <- iris2$Sepal.Length+iris2$Sepal.Width
iris2$비고 <- '..'
iris2$비고 <- NULL
iris2[,c(2:4)] <- NULL
iris2[,-2] <- NULL
iris2

# 결측치
v1 <- c(1,2,NA,3)
v1
sum(v1, na.rm = T) # NA과의 합은 유효하지 않다.그래서 na.rm = T를 해줌
v2 <- c(1,2,NULL,3) # NULL
v2
sum(v2)

# 112p 혼자서해보기
mpg1 <- mpg
mpg1 <- rename(mpg1,city = cty, highway = hwy)
mpg1

# 변수의 요약
# 범주형 변수
g = c('남','여','여','남','여','여','여','남','남')
g <- factor(g)
g
# table():빈도표생성
t<-table(g)
t

# 그래프
barplot(t)
pie(t, col = 'deepskyblue')
# 상대빈도
prop.table(t)
# 수치형 변수
score = c(60,78,83,74,100,80,90,85,70,0,300)
sort(score)
sort(score, decreasing = T)
summary(score)
boxplot(score)
hist(score)
mpg
str(mpg)
mpg$total = (mpg$cty+mpg$hwy)/2
head(mpg)
mpg$test <- ifelse(mpg$total>=20,'pass','fail')
t <- table(mpg$test)
barplot(t)
qplot(mpg$test)

#---------------------
mpg$test2 <- ifelse(mpg$total>=30,'a',ifelse(mpg$total>=25,'b',ifelse(mpg$total>=20,'c','d')))
qplot(mpg$test2)
