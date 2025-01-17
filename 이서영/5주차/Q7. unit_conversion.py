"""
당신은 어떤 그래픽 처리 라이브러리를 제작하고 있다. 라이브러리의 사용자는 다양한 단위를 이용해 데이터를 입출력하기 때문에 이 라이브러리에는 단위 변환기가 포함되어야 한다.
아래 조건에 따라 단위 변환 함수를 제작하라.
단위 변환기는 다음 단위들을 입력받아 다른 단위로 변환할 수 있어야 한다.

inch(인치)
cm(센티미터)
mm(밀리미터)
px(픽셀)
pt(포인트)
dxa(20분 포인트)
emu(EMU)

당신은 변환율 상수를 꼭 필요한 만큼만 정의할 생각이다. 라이브러리의 메모리 사용량을 최소화하는 목적도 있고, 여러 개의 상수를 손으로 입력하다 보면 실수로 버그를 만들 위험도 있기 때문이다.
당신은 백과사전을 뒤져서 믿을 수 있는 변환율 여섯 개를 찾아냈다. 당신은 아래에 있는 변환율만을 정의하여야 하며, 각 단위에서 다른 단위로 모든 경우의 변환을 지원해야 한다.

1 inch  =  2.54 cm
1 cm    =    10 mm
1 inch  =    72 pt
1 inch  =    96 px
1 pt    =    20 dxa
1 dxa   =   635 emu

입력: 단위 변환기는 두 개의 인수를 입력받는다. 첫 번째 인수는 한 단위의 수를 표현한 문자열이고 두 번째 인수는 변환하고자 하는 단위를 표현한 문자열이다.
출력: 변환된 수와 단위를 문자열로 출력한다.

입출력예:

param1         param2     result
===================================
"10 cm"        "cm"       "10 cm"

"10 inch"      "mm"       "254 mm"

"1024 px"      "pt"       "768 pt"

"768 px"       "inch"     "8 inch"

"9144000 emu"  "inch"     "10 inch"

"12000 dxa"    "px"       "800 px"
"""

"""
========================================================================
과제1. 아래의 입력에 대한 mm, pt, px, dxa, emu로 변환한 값을 출력하여라. 
     - input_unit = 10 inch
     - 출력값 : 254 mm, 720 pt, 960 px, 14400 dxa, 9144000 emu
========================================================================
"""

def convert (num,current,target): # 전환함수
    arr = [['inch','cm',2.54],['cm','mm',10],['inch','pt',72],\
            ['inch','px',96],['pt','dxa',20],['dxa','emu',635]]         # arr = 변환율
    while True:                                                     # 무한반복
        if current==target:                                         # current가 target과 같다면,(단위 변환을 하지 않아도 된다면)
            break                                                   # 반복문 멈춤
        else:                                                       # current가 target과 같지 않다면,(단위 변환을 해야한다면)
            for k in arr:                                               # arr만큼 반복
                if current in k:                                        # current가 k에 있다면,
                    if k.index(current)==0:                                 # k에서 current위치가 0일 경우 
                        num *= k[2]                                         # num = num * k[2]
                        current = k[1]                                      # current = k[1]
                    elif k.index(current)==1:                               # k에서 current위치가 1일 경우
                        num *= 1/k[2]                                       # num = num * 1/k[2]
                        current =k[0]                                       # current = k[0]
                if current in k and target in k:                        # currnet가 k에 있고, target이 k에 있을 경우,
                    break                                                   # 반복문 멈춤
        if current in k and target in k:                            # current가 k에 있고 target이 k에 있을 경우,
            break                                                   # 반복문 멈춤
    return num                                                      # num 반환

param1 = input("input_unit: ").split(" ")
param2 = [ 'mm', 'pt', 'px', 'dxa', 'emu' ]
print_result = []

for x in param2:
    result = (round(convert(int(param1[0]),param1[1],x)), x)        # param1[0]:num, param1[1]:current, param2:target
    print_result.append(result)

for i in print_result :
    for j in i:
        print(j, end = '')
    if print_result.index(i) < len(print_result)-1: # 만약 print_result 중 i의 순서가 print_result의 길이보다 작으면
        print(', ', end = '')                       # ','와 함께 출력, 출력값을 한줄로 출력하기 위해 end = '' 사용 
    else:                                           # 아닐경우
        print()                                     # 출력

"""
========================================================================
과제2. input_unit을 trans_unit의 단위로 변환한 값을 출력하여라. 
     - input_unit = '768 px'
     - trans_unit =  'inch'
     - 출력값 : 8 inch
========================================================================
"""

def convert (num,current,target): # 전환함수
    arr = [['inch','cm',2.54],['cm','mm',10],['inch','pt',72],\
            ['inch','px',96],['pt','dxa',20],['dxa','emu',635]]         # arr = 변환율
    while True:                                                     # 무한반복
        if current==target:                                         # current가 target과 같다면,(단위 변환을 하지 않아도 된다면)
            break                                                   # 반복문 멈춤
        else:                                                       # current가 target과 같지 않다면,(단위 변환을 해야한다면)
            for k in arr:                                               # arr만큼 반복
                if current in k:                                        # current가 k에 있다면,
                    if k.index(current)==0:                                 # k에서 current위치가 0일 경우 
                        num *= k[2]                                         # num = num * k[2]
                        current = k[1]                                      # current = k[1]
                    elif k.index(current)==1:                               # k에서 current위치가 1일 경우
                        num *= 1/k[2]                                       # num = num * 1/k[2]
                        current =k[0]                                       # current = k[0]
                if current in k and target in k:                        # currnet가 k에 있고, target이 k에 있을 경우,
                    break                                                   # 반복문 멈춤
        if current in k and target in k:                            # current가 k에 있고 target이 k에 있을 경우,
            break                                                   # 반복문 멈춤
    return num                                                      # num 반환

param1 = input("input_unit: ").split(" ")
param2 = input("trans_unit: ")
result = convert(int(param1[0]),param1[1],param2) # param1[0]:num, param1[1]:current, param2:target
print('출력값: ', round(result), param2)

""""
========================================================================
과제3. 아래의 입력에 대한 변환한 값을 출력하여라.
     - 조건 1 : input_unit과 trans_unit을 input() 함수를 사용하여 입력받는다.
     - 조건 2 : 입력 - 출력 - 입력 - 출력을 반복하는 코드를 작성하고, 반복 횟수는 4번이다.
     
     input_unit   trans_unit     출력값  
     "10 cm"        "cm"       "10 cm"

     "10 inch"      "mm"       "254 mm"

     "1024 px"      "pt"       "768 pt"

     "768 px"       "inch"     "8 inch"
========================================================================
"""
def convert (num,current,target): # 전환함수
    arr = [['inch','cm',2.54],['cm','mm',10],['inch','pt',72],\
            ['inch','px',96],['pt','dxa',20],['dxa','emu',635]]         # arr = 변환율
    while True:                                                     # 무한반복
        if current==target:                                         # current가 target과 같다면,(단위 변환을 하지 않아도 된다면)
            break                                                   # 반복문 멈춤
        else:                                                       # current가 target과 같지 않다면,(단위 변환을 해야한다면)
            for k in arr:                                               # arr만큼 반복
                if current in k:                                        # current가 k에 있다면,
                    if k.index(current)==0:                                 # k에서 current위치가 0일 경우 
                        num *= k[2]                                         # num = num * k[2]
                        current = k[1]                                      # current = k[1]
                    elif k.index(current)==1:                               # k에서 current위치가 1일 경우
                        num *= 1/k[2]                                       # num = num * 1/k[2]
                        current =k[0]                                       # current = k[0]
                if current in k and target in k:                        # currnet가 k에 있고, target이 k에 있을 경우,
                    break                                                   # 반복문 멈춤
        if current in k and target in k:                            # current가 k에 있고 target이 k에 있을 경우,
            break                                                   # 반복문 멈춤
    return num                                                      # num 반환

for x in range(4):
    param1 = input("input_unit: ").split(" ")
    param2 = input("trans_unit: ")
    result = convert(int(param1[0]),param1[1],param2) # param1[0]:num, param1[1]:current, param2:target
    print('출력값: ', round(result), param2)