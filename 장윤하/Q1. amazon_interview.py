'''
다음과 같은 형태의 배열을

[a1,a2,a3...,an,b1,b2...bn]
다음과 같은 형태로 바꾸시오

[a1,b1,a2,b2.....an,bn]
'''
"""
========================================================================
과제1. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 사용 X
      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = input("리스트를 입력하세요: ").split(',')      # 콤마를 기준으로 분리하여 저장
a_plus_b = len(input_list) // 2                         # 길이를 반으로 나누어 저장

output_list = []                                        # 결과 리스트를 생성
for i in range(a_plus_b):                               # 길이를 반으로 나눈 만큼 반복
    output_list.append(input_list[i])                   # 리스트의 i번째, 즉 a중 i번째 값을 리스트에 저장
    output_list.append(input_list[i + a_plus_b])        # b의 i번째 값을 리스트에 저장 (ex. b1은 a1 인덱스에 길이를 2로 나눈 값을 더한 만큼의 인덱스에 위치)

print(output_list)

"""
========================================================================
과제2. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']

print(sorted(input_list, key = lambda x: int(x[1:])))       # 각 문자열의 알파벳을 제외한 숫자를 기준으로 정렬하여 리스트 프린트

"""
========================================================================
과제3. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 사용 X
      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
a_list = []             # a를 저장할 리스트
b_list = []             # b를 저장할 리스트

for i in input_list:                # input_list를 반복하면서
    if 'a' in i:                    # 각 문자에 a가 존재하는 경우
        a_list.append(i)            # a리스트에 저장
        a_list.sort()               # 리스트 정렬
    elif 'b' in i:                  # b가 문자에 존재하는 경우
        b_list.append(i)            # b리스트에 저장
        b_list.sort()               # b리스트 정렬

output_list = []                    # 결과를 저장할 리스트 저장
for j in range(len(input_list)//2): # 리스트를 반으로 나눈 길이만큼 반복
    output_list.append(a_list[j])   # a리스트와 b리스트의 j번째 값을 순서대로 결과 리스트에 저장
    output_list.append(b_list[j])

print(output_list)                  # 결과 리스트 프린트

"""
========================================================================
과제4. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']

input_list = sorted(input_list, key = lambda x: int(x[1:]))                     # 각 문자열의 알파벳을 제외한 숫자를 기준으로 정렬한 리스트 저장
for i in range(0, len(input_list), 2):                                          # 0부터 2씩 증가시키면서 반복 (두 쌍의 문자 중 첫 번째 문자의 인덱스)
    if 'b' in input_list[i]:                                                    # 해당 문자가 b를 포함할 경우
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]     # b를 a 뒤로 보내기 위해 a와 b의 자리를 바꾼다
print(input_list)
