fp1 = open('hoseo.txt','r') # 원본
fp2 = open('hoseo_copy.txt','w') #복사본

temp = fp1.readlines()# 원본파일 리스트에 저장

    
for line in temp:
    print(line,file = fp2, end ='')
    
fp1.close()
fp2.close()
