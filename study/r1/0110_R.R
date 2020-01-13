library(xlsx)
install.packages('rJava')
Sys.setenv(JAVA_HOME='C:/Program Files/Java/jdk1.8.0_221')
library(rJava)
install.packages('readxl')
library(readxl)
df <- read_excel('food1.xlsx')
df<- read.xlsx2('food1.xlsx',sheetIndex = 1)
df
head(df)
str(df)
head(df$'소재지전체주소')
df$dong <- substr(df$'소재지전체주소',11,14)
df$dong <-gsub('[0-9]','',df$dong)
df$dong <- gsub(' ','',df$dong)
View(df)
str(df)
table(df$dong)
df2<- data.frame(table(df$dong))
df2
install.packages('treemap')
library(treemap)
# treemap(데이터프레임, index='기준열', vSize='값', title='제목')
treemap(df2, index = 'Var1', vSize = 'Freq', title = '구로구 치킨집개수')
library(dplyr)
df2 %>% arrange(desc(Freq))
#--------------------------
df<-read_excel('air.xlsx')
head(df)
str(df)
df1 <- df %>% filter(측정소명=='구로구'|측정소명=='도봉구')
df1
View(df1)
table(df1$측정소명)
guro <- df1 %>% filter(측정소명=='구로구')
dobong <- df1 %>% filter(측정소명=='도봉구')
boxplot(guro$미세먼지, dobong$미세먼지, names = c('구로구','도봉구'), main = '18년도 4분기 미세먼지 비교')


#---------------오라클 연동
install.packages("DBI")
install.packages("RJDBC")
library(DBI)
library(rJava)
library(RJDBC)
drv<-JDBC("oracle.jdbc.driver.OracleDriver","D:/app/hong/virtual/product/12.2.0/dbhome_1/jdbc/lib/ojdbc8.jar")
conn<-dbConnect(drv,'jdbc:oracle:thin:@127.0.0.1:1521/orcl',"c##java00","java00")

#select
sql <- "select * from emp where sal>2000"
data<-dbGetQuery(conn,sql)
sql <- "select * from emp order by job"
str(data)

#insert
sql<- "insert into emp values(1,'둘리','사원',7566,sysdate,100,0,30)"
dbSendUpdate(conn,sql)
sql<-"select * from emp"
dbGetQuery(conn,sql)

#update
sql<-"update emp set sal=9999 where deptno=20"
dbSendUpdate(conn,sql)

#delete
sql<-"delete from emp where job ='MANAGER'"
dbSendUpdate(conn,sql)
dbDisconnect(conn) # 연결종료
#-----------------------------

df<- read.csv(file='전처리.csv',header = T)
df
str(df)
head(df$age)
head(df['age'])
head(df[4])
head(df[c('gender','job')])
head(df[c(2:4)])
head(df[-4])
summary(df)
mean(df$age,na.rm = T)

#결측치 제거하는 함수 omit
nae<-na.omit(df$age) 
nae2<-df %>% filter(!is.na(age))
nae2
length(nae)
length(df$age)
df1<-na.omit(df)
str(df1)

#----------------결측치 0으로
df$price
df$price2 <- ifelse(is.na(df$price),0,df$price)
View(df)

#---------결측치를 평균으로
df$price3 <- ifelse(is.na(df$price),round(mean(df$price, na.rm = T)),df$price)
df[c('price','price2','price3')]
# 이상치 처리
summary(df)
table(df$gender)
df2<-subset(df,gender==1|gender==2)
str(df2)
boxplot(df$price)
df2<-subset(df2,price>=2 & price<=8)
str(df2)
boxplot(df2$price)
# 나이(20~69)
summary(df2)
df2<- subset(df2,age >=20 & age <=69)
str(df2)

# 170p
library(ggplot2)
mpg[c(65,124,131,153,212),"hwy"] <- NA
# 1번
table(is.na(c(mpg$drv,mpg$hwy)))

# 2번
mpg %>% filter(!is.na(mpg$hwy)) %>% group_by(trans) %>% summarise(mean_hwy=mean(hwy)) %>% arrange(desc(mean_hwy))

# 178p
mpg[c(10,14,58,93),"drv"]<-'k'
mpg[c(29,43,129,203),'cty']<-c(3,4,39,42)
# 1번
table(mpg$drv)
mpg$drv <- ifelse(mpg$drv %in% 'k',NA,mpg$drv)

#2번
boxplot(mpg$cty)
quantile(mpg$cty, na.rm = T)
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)
table(mpg$cty)

#3번
mpg %>% filter(!is.na(drv) & !is.na(cty)) %>% group_by(drv) %>% summarise(mean_cty=mean(cty))















