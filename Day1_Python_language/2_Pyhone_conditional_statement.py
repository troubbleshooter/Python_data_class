#number = 11
#number = int(input())  #input()의 경우 Str문자형으로 인식하므로, 정수형 int()로 변환
#if number < 5:
#    print("숫자가 5보다 작습니다.")
#elif 5 < number < 10:
#    print("숫자가 5보다 크고 10보다 작습니다.") 
#else:
#    print("숫자가 10보다 큽니다.")

"""    
money = int(input())

if money >= 70000:
    print("비행기")
elif 50000 <= money < 70000:
    print("기차")
elif 30000 <= money < 50000:
    print("버스")
elif money < 30000:
    print("도보")
"""
#for i in range(10): #for each ITEM in [LIST]/range(number of items/variables)/"string"(each letters): do something
 #   print("Hello world")

'''
countries = ["kor", "usa", "hk"]
for country in countries:
    if country == "kor":
        print("한글로 보여주세요.")
    elif country == "usa":
        print("영어로 보여주세요.")
    elif country == "hk":
        print("중국어로 보여주세요.")
'''
## WHILE loop executes a set of statements as long as a condition is true. Refresh. eg) KTX
'''
a = 0
while a < 5:
    a = a + 1
    print(a)
    
#is_ticket = False
#while is_ticket == True:
'''

#Q.1부터 5까지 더하는 프로그램을 만들어보시오. i = 1+2+3+4+5

'''
x = 0
for i in range(1,6):
    x = x + i    # same as x += i
    if  1 <= i < 5:
        continue    # = skip, comes with IF : and CONTINUE
    print(x)
    
x = 0
for i in range(1,6):
    x = x + i    # same as x += i
print(x)

result = 0
i = 1
while i < 6:
		result = result + i
		i += 1  # i= i+1
		print(result)


for i in range(1,11):
    if 3<= i <=5:
        continue    # keep looping when i is 3,4,5 = skip 
    print(i)
'''
for i in range(1,11):
    if 3<= i <=5:
        break    # stop when i reach to 3 
    print(i)