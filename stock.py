
import requests
import re

# header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
# url="https://finance.naver.com/item/main.naver?code={company_code}".format(company_code)
# res= requests.get(url, headers=header)
# res.raise_for_status # error happen-> halt
 

list_1=[] # text에서 가공하지 않은 기업 리스트
enterprise_list=[]
enterprise_list_1=[]#종목코드와 기업 이름을 가진 리스트를 가진 리스트, 즉 2중 리스트




with open("company.txt", "r", encoding ="utf8") as f:#종목코드 및 종목코드 외부 파일에서 불러오기

    lines = f.readlines()
    for line in lines:
        if line == '\n':
            continue
        list_1.append(line)

    for elements in list_1:#한글자씩 쪼개서 \n제거 후 재결합
        elements=list(elements)
        a=str(elements[0])
        for i in range(1,len(elements)-1):
            a=a+str(elements[i])
        enterprise_list.append(a)
    for i in range(0,len(enterprise_list)):
        a=str(enterprise_list[i]).split(":")
        enterprise_list_1.append(a)

#문자열 안 공백 제거
for i in range(0,1747):
    for j in [0,1]:
        str(enterprise_list_1[i][j]).strip()
    

#여기부터 계속 이어서 하기-> 리스트에 포함된 공백 제거 해야함






class calculate():
    
    print("프로그램이 실행 됨")
    def __init__(self):
        print("보유하고 있는 종목의 이름 또는 종목코드를 입력하십시오")
        
        self.en_code_list=[]#en:company
        while True:
            self.en=input()
            if type(self.en) == int:
                self.en_code_list.append(self.company)
            elif type(self.en )== str:
                if self.en == "입력완료":
                    break
                #self.en_code_list.append(enterprise_list_1[1].index(self.en))#기업이름을 코드로 환산 후 리스트에 추가
                print(enterprise_list_1[1].index(self.en))




        
        print(self.en_code_list)

print(enterprise_list_1)





        



            


            
        

        



    