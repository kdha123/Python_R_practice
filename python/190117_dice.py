import random



dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = 0
if dice1 == dice2 :
    dice3 = random.randint(1,6)
print('1번',dice1,'2번',dice2,'3번',dice3)
print(dice1+dice2+dice3,'칸이동')   

   

