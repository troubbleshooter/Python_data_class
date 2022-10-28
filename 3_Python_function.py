"""
def name(input):    # = def name(input = "예원")
    print("제 이름은 " + input + "입니다.")

name("예원")
"""
"""
def sum(a,b):
    print("a+b")
    print(a+b)
    return a+b

total = sum(3,4)
print("total")
print(total)
"""

#Q.성적과 이름을 입력하고, 성적에 따른 등급을 알려주는 프로그램을 만드시오.

#90점 이상 A등급
#80점 이상 B등급
#70점 이상 C등급
#60점 이상 D등급
#60점 미만 F등급

'''
def check_grade(성적, 이름):
    if 성적 >=90:
        print(이름 + "의 등급은 A입니다.")
    elif 성적 >=80:
        print(이름 + "의 등급은 B입니다.")
    elif 성적 >= 70:
        print(이름 + "의 등급은 C입니다.")
    elif 성적 >= 60:
        print(이름 + "의 등급은 D입니다.")
    elif 성적 <60:
        print(이름 + "의 등급은 F입니다.")

check_grade(1, "이예원")
'''
'''range()
len()
print()'''

a="python"
a=a.upper()
print(a)