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


# 입문 문제 - 한 번만 등장한 문자
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

'''
제한사항
0 < s의 길이 < 1,000
s는 소문자로만 이루어져 있습니다.
'''

def solution(s):
    answer = ''
    list = []
    b_list = []
    total_list = []
    for i in s:
        if i not in list:
            list.append(i)
        else:
            b_list.append(i)
            
    for l in s:
        if l not in b_list:
            total_list.append(l)
            total_list.sort()
    answer = ''.join(total_list)
    return answer


# 입문 문제 - 7의 개수
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    answer = 0
    word = ''.join(str(e) for e in array)
    for i in word:
        if int(i) == 7:
            answer += 1
    return answer



# 입문 문제 - 컨트롤 제트
# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 
# 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

'''
s는 숫자, "Z", 공백으로 이루어져 있습니다.
s에 있는 숫자와 "Z"는 서로 공백으로 구분됩니다.
연속된 공백은 주어지지 않습니다.
0을 제외하고는 0으로 시작하는 숫자는 없습니다.
s는 "Z"로 시작하지 않습니다.
s의 시작과 끝에는 공백이 없습니다.
"Z"가 연속해서 나오는 경우는 없습니다.
'''

def solution(s):
    answer = 0
    s = s.split()
    
    num_list = []

    for i in s:
        try :
            if float(i):
                num_list.append(int(i))
        except:
            
            if num_list:
                num_list.pop(-1)
            
    answer = sum(num_list)    

    return answer