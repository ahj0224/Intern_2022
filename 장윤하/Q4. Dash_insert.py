"""
-----------------  Question  -----------------
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤,
문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
(예, 454 => 454, 4546793 => 454*67-9-3)
DashInsert 함수를 완성하자.

입력 - 화면에서 숫자로 된 문자열을 입력받는다. : "4546793"
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다. : "454*67-9-3"
----------------------------------------------
"""
# 과제 1. 함수를 만들지 말고, 위 문제를 풀어보세요.
## input = "336917411"
## 출력 : 3-369-1-741-1


a = input("input = ") # 변수 a에 입력값 저장
b = [] # b라는 리스트 생성

for i in range(1, len(a)): # a 길이만큼 반복
    if int(a[i-1]) % 2 == 0:   # a의 (i-1)번째 자릿수가 짝수인 경우 
        if int(a[i]) % 2 == 0: # 그 다음 자릿수도 짝수인 경우
            b.append(a[i-1] + '*') # a의 i-1번째 숫자 뒤에 *를 추가하여 b에 저장
        else:
            b.append(a[i-1]) # 아닌 경우는 숫자만 저장 
    
    else:                      # a의 (i-1)번째 자릿수가 홀수인 경우 
        if int(a[i]) % 2 == 1: # 그 다음 자릿수가 홀수인 경우
            b.append(a[i-1] + '-') # a의 i-1번째 숫자 뒤에 -를 추가하여 b에 저장
        else:
            b.append(a[i-1]) # 아닌 경우는 숫자만 저장

print("".join(b)+str(a[-1])) # b에 저장된 값을 하나의 문자열로 합친 값과 마지막 값을 함께 출력
    

#과제 2. 함수를 만들어서 위 문제를 풀어보세요.(함수명은 "DashInsert"로 지정하세요)
## input = "13221478898889212122"
## 출력 :  1-32*21478*898*8*8921212*2

def DashInsert():
    a = input()
    b = []

    for i in range(1, len(a)):
        if int(a[i-1]) % 2 == 0:
            if int(a[i]) % 2 == 0:
                b.append(a[i-1] + '*')
            else:
                b.append(a[i-1])
        
        else:
            if int(a[i]) % 2 == 1:
                b.append(a[i-1] + '-')
            else:
                b.append(a[i-1])
    print("".join(b),a[-1])
    
DashInsert()




