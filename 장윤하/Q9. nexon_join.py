"""
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
n을 d(n)의 제네레이터(generator)라고 한다.
예를 들어 d(91) = 9 + 1 + 91 = 101인 경우 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.

예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
"""

"""
==========================================================================
# 과제 1. 1부터 30까지의 자연수 중에서, 제너레이터가 있는 수의 합을 구하시오. 
## 출력 : 420
==========================================================================
==========================================================================
# 과제 2. 1이상 5000 미만의 셀프 넘버(제너레이터가 하나도 없는 수)의 합을 구하시오.
## 출력 : 1227365
==========================================================================
"""

#1

def d_fn(n): # 각 자리 숫자와 자기 자신을 더하는 함수
    s = str(n) # n 값을 문자열로 저장 
    re = 0
    for x in range(len(s)): # 문자열 길이만큼 반복 
        re += int(s[x])     # 각 자릿수 숫자를 더함
    return re + n           # 각 자릿수 숫자와 자기 자신을 더한 수를 반환

Z = [d_fn(n) for n in range(31)]  # 30까지 자연수의 각 자리 숫자와 자기 자신을 더한 값을 저장


sum = 0

for i in range(30): # 30번 반복
    if Z[i] <= 30:  # Z의 값이 30 이하인 경우
        sum += Z[i] # 값을 더함
print(sum)

#2



Z1 = [d_fn(n) for n in range(5001)] # 5000까지 자연수의 각 자리 숫자와 자기 자신을 더한 값을 저장

sum = 0
for j in range(5001): # 5000까지의 자연수 중
    if j not in Z1:   # Z1에 포함되지 않은 수를 합함
        sum += j
print(sum)


