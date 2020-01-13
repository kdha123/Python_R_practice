df2
table(df2$resident)
df2$resident2[df2$resident==1]<- '서울'
df2$resident2[df2$resident==2]<- '인천'
df2$resident2[df2$resident==3]<- '대전'
df2$resident2[df2$resident==4]<- '대구'
df2$resident2[df2$resident==5]<- '시구군'
View(df2)
# df2$job2 컬럼 생성, 1이면 공무원, 2이면 회사원, 3이면 개인사업
df2$job2[df2$job==1]<- '공무원'
df2$job2[df2$job==2]<- '회사원'
df2$job2[df2$job==3]<- '개인사업'
 
# df2$age2 컬럼 생성, 30이하 청년층, 30초과 55이하 중년층, 55초과 장년층
df2$age2[df2$age<=30]<- '청년층'
df2$age2[df2$age>30 & df2$age <= 55]<- '중년층'
df2$age2[df2$age> 55]<- '장년층'

#--두범주형 변수의 관계
df<- read.csv('age.txt')
df
table(df$GENDER)
table(df$AGE)
t1<-table(df$GENDER, df$AGE)
barplot(t1, legend=T, col = rainbow(2))
barplot(t1, legend=T, col = rainbow(2), beside = T)

#-------------------------
bloodType <- c('A','B','A','AB','O','A','O','B','A','O','O','B','O','A','AB','B','O','A','A','B')
name=c("kim","park","lee","kim","park","lee","kim","park","lee","kim","park","lee","kim","park","lee","kim","park","lee","choi","lee")
gender=c("남","여","남","여","남","여","남","여","남","여","남","여","남","여","남","여","남","여","남","여")
df <- data.frame(name, gender, bloodType)
df
t1<- table(df$gender, df$bloodType)
t1
barplot(t1, legend = T, col=rainbow(2))

# 수치형 변수의 관계(산점도 이용)
df<- read.csv('study.txt')
df
plot(df$HOUR, df$SCORE, pch=16, col='red')

#상관계수(-1~1, 1에 가까울수록 양의 상관관계가 강함)
cor(df$HOUR, df$SCORE)
iris
plot(iris$Sepal.Length, iris$Sepal.Width)
cor(iris$Sepal.Length,iris$Sepal.Width)

# 범주형 변수와 수치형 변수의 관계
df<-read.csv('score.txt')
df
aggregate(SCORE~CITY, data =df,mean )
boxplot(SCORE~CITY,data = df)
#---------------------
library(ggplot2)
View(mpg)

# 1.배경설정
ggplot(data=mpg,aes(x=displ, y=hwy))
# 2. 그래프
ggplot(data=mpg,aes(x=displ, y=hwy))+geom_point()

# 3. 상세설정
ggplot(data=mpg,aes(x=displ,y=hwy))+
  geom_point()+
  xlim(3,6)+
  ylim(10,30)

####구동방식(drv)별 평균 고속도로 연비(hwy)
library(dplyr)
mpg2<-mpg %>% group_by(drv) %>% summarise(avg=mean(hwy))
ggplot(data=mpg2,aes(x=drv,y=avg))+geom_col()
ggplot(data=mpg, aes(x=drv, y=hwy))+geom_boxplot()

# x축 정렬
ggplot(data=mpg2,aes(x=reorder(drv,avg),y=avg))+geom_col()
ggplot(data=mpg2,aes(x=reorder(drv,-avg),y=avg))+geom_col()
table(mpg$drv)
ggplot(data = mpg,aes(x=drv))+geom_bar()

# 데이터 분석 절차 : 변수검토 및 전처리 -> 변수간의 관계분석-------------
install.packages('foreign')
library(foreign)
df <- read.spss(file='Koweps_hpc10_2015_beta1.sav', to.data.frame = T)
View(df)
str(df)
library(dplyr)
df <- rename(df,
             sex=h10_g3,
             birth=h10_g4,
             marriage=h10_g10,
             religion=h10_g11,
             code_job=h10_eco9,
             income=p1002_8aq1,
             code_region=h10_reg7)

# 성별에 따른 월급차이
head(df$sex)
summary(df$sex)
table(df$sex)
df$sex2[df$sex==1]<-'남자'
df$sex2[df$sex==2]<-'여자'
table(df$sex2)
qplot(df$sex2)
summary(df$income)
df$income2 <- ifelse(df$income>=1 & df$income<=9998,df$income,NA)
sex_income <- df %>%
  filter(!is.na(income2)) %>%
  group_by(sex2) %>%
  summarise(avg_income=mean(income))
ggplot(data= sex_income, aes(x = sex2, y=avg_income))+geom_col()

# 나이와 월급의 관계
summary(df$birth)
qplot(df$birth)
df$age <- 2015-df$birth+1
age_income <- df %>%
  filter(!is.na(income)) %>%
  group_by(age) %>%
  summarise(avg_income = mean(income))
ggplot(data = age_income, aes(x =age, y= avg_income))+geom_line()

#연령대에 따른 월급의 차이
df$ageg[df$age<30]<-'초년'
df$ageg[df$age>=30 & df$age <=59]<-'중년'
df$ageg[df$age>60]<-'노년'
ageg_income <- df %>%
  filter(!is.na(income)) %>%
  group_by(ageg)%>%
  summarise(avg_income=mean(income))
ggplot(data = ageg_income,aes(x=ageg, y=avg_income))+geom_col()+scale_x_discrete(limits=c('초년','중년','노년'))

# 연령대 및 성별에 따른 월급차이
ageg_sex_income<-df %>%
  filter(!is.na(income)) %>%
  group_by(ageg,sex2) %>%
  summarise(avg_income=mean(income))
ageg_sex_income
ggplot(data = ageg_sex_income,aes(x=ageg,y=avg_income), fill=sex2)+geom_col(position = 'dodge')+scale_x_discrete(limits=c('초년','중년','노년'))

# 나이 및 성별에 따른 월급차이
age_sex_income<-df %>%
  filter(!is.na(income)) %>%
  group_by(age,sex2) %>%
  summarise(avg_income=mean(income))
age_sex_income
ggplot(data = age_sex_income,aes(x=age,y=avg_income, col=sex2))+geom_line()

# 193p 1번
suv_cty<-mpg %>% filter(class=='suv') %>% group_by(manufacturer) %>% summarise(mean_cty=mean(cty)) %>% arrange(mean_cty) %>% head(5)
ggplot(data=suv_cty,aes(x=manufacturer, y=mean_cty))+geom_col()

# 193p 2번
ggplot(data=mpg,aes(x = class))+geom_bar()

# 198p 1번
class_cty <- mpg %>% filter(class %in% c('compact','subcompact','suv')) 
ggplot(data=class_cty,aes(x= class ,y= cty))+geom_boxplot()

#직업별 월급차이
table(df$code_job)
summary(df$code_job)
library(readxl)
listjob <-read_excel('Koweps_Codebook.xlsx',sheet = 2)
head(listjob)
df<-left_join(df,listjob,id='code_job')
head(df[c('code_job','job')])
job_income <- df %>%
  filter(!is.na(job) & !is.na(income)) %>% 
  group_by(job) %>%
  summarise(avg_income = mean(income))
top10<-job_income %>% arrange(desc(avg_income)) %>% head(10)
ggplot(data=top10,aes(x=job,y=avg_income))+geom_col()+coord_flip()
bottom10<-job_income %>% arrange(desc(avg_income)) %>% tail(10)
ggplot(data=bottom10,aes(x=job,y=avg_income))+geom_col()+coord_flip()

# 성별 직업 빈도
df %>% filter(!is.na(job) & sex2=='남자') %>%
  group_by(job) %>% 
  summarise(cnt=n())




















