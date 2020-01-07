a <- 1 #a에 1할당
a

b<-2
b
c<-3
c
d<-3.5
d
a+b
a+b+c
4/b
5*b

var1 <- c(1,2,5,7,8) # 숫자 5개로 구성된 변수 생성성
var1
var2 <- c(1:5)
var2
var3 <- seq(1,5)
var3
var4 <- seq(1,10,by=2) # 1~10까지 2 간격 연속 값으로 변수 생성
var4
var5 <- seq(1,10, by = 3) # 1~10까지 3간격 연속 값으로 변수 생성성
var5
var1+2
var1+var2

# 문자로 된 변수 만들기
str1 <- 'a'
str1
str2 <- 'text'
str2
str3 <- 'Hello World!'
str3
str4 <- c('a','b','c')
str4
str5 <- c('hello', 'World','is','good')
str5
str1+2 # 문자는 숫자로 연산할 수 없다.

# 숫자를 다루는 함수
x <- c(1,2,3)
x
mean(x) # 평균
max(x) # 최대값
min(x) # 최소값
paste(str5,collapse = ",") # 쉼표를 구분자로 str5 단어들 하나로 합치기

x_mean <- mean(x) # 함수를 바로 실행할 수 있지만 변수에 넣을 수도 있다.
x_mean

# 패키지 사용하기
install.packages("ggplot2")
library(ggplot2)
x <- c('a','a','b','c')
qplot(x) # 빈도 막대 그래프 출력
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
