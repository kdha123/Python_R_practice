dept <- c('개발부', '개발부', '개발부', '개발부','영업부', '영업부', '영업부', '영업부')
position <- c('과장', '과장', '차장', '차장','과장', '과장', '차장', '차장')
name <- c('김가윤', '고동산', '박기성', '이소균','황가인', '최유리', '김재석', '유상균')
salary <- c(5400, 5100, 7500, 7300, 4900, 5500, 6000, 6700)
worktime <- c(15, 18, 10, 12, 17, 20, 8, 9)
df <- data.frame(dept,position,name,salary, worktime)
df
str(df)
df$name <- as.character(df$name)
str(df)
summary(df)

# aggregate(컬럼명~그룹컬럼명,데이터, 적용함수)
aggregate(salary~dept, df, mean)
aggregate(cbind(salary, worktime)~dept, df, mean)
aggregate(salary~dept+position,df,mean) # 기준이 2개일때는 "+" 사용

library(dplyr)
df %>%
  summarise(avg = mean(salary))
df %>%
  group_by(dept) %>%
  summarise(avg = mean(salary))
df %>%
  group_by(dept) %>%
  summarise(avg = mean(salary),hap=sum(salary),avgwork=mean(worktime))
df %>%
  group_by(dept,position) %>%
  summarise(avg = mean(salary),hap=sum(salary),avgwork=mean(worktime))
#-------------------
v1 <- c(100,10,200,3,11)
v1
sort(v1,decreasing = T)
df %>%
  arrange(name)
df %>%
  arrange(dept,desc(position))
df$tax <- df$salary*0.1
df %>% mutate(tax=salary*0.1,
              timesal=salary/worktime)
# 과장 중에 시급이 가장 높은 두명만 출력
df %>% 
  filter(position=='과장') %>%
  mutate(timesal=salary/worktime) %>%
  arrange(timesal) %>%
  tail(2)

#------------------
df<-read.table(file='clipboard', header = T)
str(df)
# 객실번호를 팩터로 변경
df$room_number <- as.factor(df$room_number)
# 방종류별 평균가격 출력
df %>%
  group_by(type) %>%
  summarise(mean(price))

id <- c('F2', 'F1', 'F4', 'F3')
name <- c('박지성', '김가인', '이승철', '고아라')
age <- c(24, 32, 40, 18)
df1 <- data.frame(id,name,age)

id <- c('F2', 'F1', 'F4', 'F3')
name <- c('박지성', '김가인', '이승철', '고아라')
score <- c(95, 100, 56, 73)
df2 <- data.frame(id,name,score)
df1
df2
cbind(df1,df2)
merge(df1,df2, by = c('id','name'))

s <- read.table(file='clipboard', header = T)
s
t <- read.table(file = 'clipboard', header = T)
t
merge(s,t,by='class')
left_join(s,t,by='class')

#제어문--------------------
5%%3 # 나머지
5^3 # 제곱
a=3
b=2
a==b
a!=b
#if(조건식){
  #}else{
  #}
score<-scan()
if(score > 90){
  cat(score,'-->a학점')
}else if(score>=80){
  cat(score,'-->b학점')  
}else{
  cat(score,'-->c학점')
}

# ifelse(조건, 참, 거짓)
# switch(비교구문, 실행1, 실행2,..)
switch('age',id='kdh',hobby='movie',age=26,addr='경기도')
switch('hobby',id='kdh',hobby='movie',age=26,addr='경기도')
# which(조건)
name <- c('kim','lee','park','choi')
which(name=='choi')

no <- c(1,2,3,4,5)
name <- c('kim','lee','park','choi','yun')
score<- c(90,80,85,87,70)
df <- data.frame(no,name,score)
df
which(score==90)

#for(변수 in 값){}
v1 <- c(1:10)
v1
v2 <- numeric()
v2
for(i in v1){
  # print(i*3)
  v2[i]<-i*3
}
v2
for (i in v1) {
  if(i%%2==1)
    print(i)
}

# while(조건){}
i <-1
while(i<10){
  print(i)
  i<-i+1
}

# 변수 <-function(매개변수){}

hi<-function(){
  print('hi~~')
}
hi()
hi2<-function(x){
  cat('hi~~',x)
}
hi2('kim')
df<- read.table(file = 'clipboard', header = T)
df
str(df)
summary(df)
table(df$A)
table(df$B)
dim(df)[2]
length(df)
f1<-function(d){
  for (i in 1:dim(d)[2]) {
    print(i)
    print(table(d[i]))
  }
}
f1(df)

gugudan<-function(dan){
  cat(dan,'단\n')
  for (i in 1:9) {
    cat(dan,'*',i,'=',dan*i,'\n')
  }
}
gugudan(3)

# 결측치처리------------
v1<-c(10,20,5,4,40,7,NA,6,3,NA,2,NA)
v1
mean(v1,na.rm = T)
is.na(v1)
v2<-ifelse(is.na(v1),0,v1)
mean(v2)
v3<-ifelse(is.na(v1),round(mean(v1,na.rm = T),2),v1)
v3
#---------------

v1 <- c(305,450,320,460,330,480,380,520)
colors()
barplot(v1, ylim = c(0,600), main = '그래프 제목', ylab='매출액', 
        col=c('gold','salmon','seagreen3','seashell','slategray1','violetred','yellow','violetred'))
barplot(v1, ylim = c(0,600), main = '그래프 제목', ylab='매출액', 
        col=heat.colors(8))
names(v1)<-c('18년1분기','18년2분기','18년3분기','18년4분기','19년1분기','19년2분기','19년3분기','19년4분기')
v1
barplot(v1, main = '그래프 제목', ylab='매출액', 
        col=heat.colors(8), xlab = '연도별 분기', horiz = T, space = 1, cex.name = 0.8)
VADeaths
barplot(VADeaths, col = rainbow(5))
barplot(VADeaths, col = rainbow(5), beside = T, main ='사망률')
legend(20,70,c('50-54','55-59','60-64','65-69','70-74'),fill = rainbow(5),cex=0.7)
pie(v1, col = rainbow(8), border = 'red')
boxplot(VADeaths)
storeA<- c(20,21,23,22,26,28,35,35,41,42,43,45,44,45,46,47,47,46,47,58,58,59,60,56,57,57,80)
storeB<- c(5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70,600)
mean(storeB) # 50.5
boxplot(storeA)
boxplot(storeB)
mean(storeB[storeB<600])
storeB <- storeB[storeB<600]
boxplot(storeB)
boxplot(storeA, storeB, names = c('A식당','B식당'))
hist(storeA)
hist(storeB)

# 분산: 평균으로부터 떨어진 정도
var(storeA)
var(storeB)

# 표준편차
sd(storeA)
sd(storeB)
hist(storeB,breaks = 4)

# 133p, 141p, 150p
library(ggplot2)
library(dplyr)
# 133p
# 배기량이 4, 5인 자동차 중 고속도로 연비 4이하인게 더 연비가 높음
mpg %>% filter(displ<=4) %>% summarise(mean(hwy))
mpg %>% filter(displ>=5) %>% summarise(mean(hwy))
# toyota가 연비가 더 높다.
mpg %>% filter(manufacturer =='audi') %>% summarise(mean(cty))
mpg %>% filter(manufacturer == "toyota") %>% summarise(mean(cty))
# 세개 회사의 전체 고속도로 연비
mpg %>% filter(manufacturer %in% c('chevrolet','ford','honda')) %>% summarise(mean(hwy))

# 141p
#아우디 모델의 고속도로연비 5순위
mpg %>% 
  filter(manufacturer =='audi') %>% 
  arrange(desc(hwy)) %>%
  head(5)

# 150p
#class별 cty
mpg %>% group_by(class) %>% summarise(mean(cty))

# 평균이 높은 순으로 정렬
mpg %>% group_by(class) %>% summarise(mean_cty=mean(cty)) %>% arrange(desc(mean_cty))

# 제조사 hwy평균
mpg %>% group_by(manufacturer) %>% summarise(mean_hwy=mean(hwy)) %>% arrange(desc(mean_hwy)) %>% head(3)

# compact 가장 많이 생산
mpg %>% group_by(manufacturer) %>% filter(class=='compact') %>% summarise(car_count=n()) %>% arrange(desc(car_count))


