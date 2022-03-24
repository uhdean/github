letters = 'python' 
print(letters[0],letters[2]+'\n')


string = "PYTHON"
print(string[::-1]+'\n')


url = "http://sharebook.kr"
domain = url.split('.')
print(domain[-1]+'\n')


file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
print('\n')

file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith("2020"))
print('\n')


# score = int(input("점수 입력: "))

# if score >= 0 and score <=20:
#     print('학점은 E입니다.')
# if score > 20 and score <=40:
#     print('학점은 D입니다.')
# if score > 40 and score <=60:
#     print('학점은 C입니다.')
# if score > 60 and score <=80:
#     print('학점은 B입니다.')
# if score > 80 and score <=100:
#     print('학점은 A입니다.')

cook = ["피자", "김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print('메뉴 갯수는',len(cook),'개입니다.'+'\n')


warn_investment_list = ["Microsoft","Google","Naver","Kakao","Samsung","LG"]

write_name = input('종목명을 입력해주세요.')

if write_name in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다.','\n')


list_1 = [100, 200, 300]

for tax in list_1:
    print(tax+10,'\n')

invest = ["SK하이닉스","삼성전자","LG전자"]

for length in invest:
    print(len(length))


        

