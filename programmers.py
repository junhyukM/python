# 입문 문제 - 숨어있는 숫자의 덧셈 (2)
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

'''
1 ≤ my_string의 길이 ≤ 1,000
1 ≤ my_string 안의 자연수 ≤ 1000
연속된 수는 하나의 숫자로 간주합니다.
000123과 같이 0이 선행하는 경우는 없습니다.
문자열에 자연수가 없는 경우 0을 return 해주세요.
'''

def solution(my_string):
    answer = 0
    temp = ''
    for n in my_string:
        if n.isdigit(): # 문자형으로 반환
            temp += n # 연속해서 숫자가 나오면 덧셈이 아닌 문자열 연결
        # temp에 값이 있는게 참일 때
        elif temp:
            answer += int(temp) # temp에 작성된 문자열을 int로 바꾸고 최종 답에 덧셈
            temp = '' # 다음 루프를 위해 temp 초기화
    if temp:
        answer += int(temp)
        
    return answer


# 입문 문제 - 진료 순서 정하기
# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
'''
제한사항
중복된 원소는 없습니다.
1 ≤ emergency의 길이 ≤ 10
1 ≤ emergency의 원소 ≤ 100
'''

def solution(emergency):
    answer = []
    emergency_dict = {}
    for idx, n in enumerate(emergency):
        emergency_dict[n] = idx
        
    temp2 = list(emergency_dict.values())
    temp = list(emergency_dict.keys())
    
    temp.sort(reverse=True)
    
    num = 1
    for i in temp:
       
        emergency_dict[i] = num
        num += 1
        
    answer = list(emergency_dict.values())
    return answer


