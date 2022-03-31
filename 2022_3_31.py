price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)): #1
    print(0 + i, price_list[i])

print()

for i in range(1,4): #2
    print(90+10*i, price_list[i])

print()

for i in range(2002,2051,4): #3
   print(i)

print()

for i in range(0,10): #4
    print(i/10)

print()

ticker = "btc_krw" #5
print(ticker.upper())

print()

file_name = "보고서.xlsx" #6
print('파일형식이 xlsx인가? : ',file_name.endswith('.xlsx'))

print()

a = "hello world" #7
print(a.split())

print()

date = "2020-05-01" #8
print(date.split("-"))

print()

상장주식수 = "5,969,782,550" #9
new = 상장주식수.replace(",","")
print(int(new))

print()

price = ['20180728', 100, 130, 140, 150, 160, 170] #10
print(price[1:8])

print()

nums = [1,2,3,4,5,6,7,8,9,10] #11
print(nums[1::2])

print()

list1 = [3, 100, 23 ,44] #12
for i in list1:
    if i%3 == 0:
        print(i)



