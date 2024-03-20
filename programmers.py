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



# 입문 문제 - 2진수 더하기
# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

'''
return 값은 이진수를 의미하는 문자열입니다.
1 ≤ bin1, bin2의 길이 ≤ 10
bin1과 bin2는 0과 1로만 이루어져 있습니다.
bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.
'''

def solution(bin1, bin2):
    answer = ''
    # 두 이진수를 십진수로 변환
    # 십진수인 두 수를 더하고
    # 그 십진수를 이진수로 변환
    num1 = str('0b' + bin1)
    num2 = str('0b' + bin2)
    
    int1 = int(num1, 2)
    int2 = int(num2, 2)
    
    total = int1 + int2
    
    answer = format(total, 'b')
    
    return answer


# 입문 문제 - 소인수 분해
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
# 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 2 ≤ n ≤ 10,000


def solution(n):
    answer = []
    temp = []
    i = 2
    while i <= n:
        if n % i == 0:
            temp.append(i)
            n = n / i
        else:
            i = i + 1
    
    for i in temp:
        if i not in answer:
            answer.append(i)
    
    return answer


# 입문 문제 - 잘라서 배열로 저장하기
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

'''
1 ≤ my_str의 길이 ≤ 100
1 ≤ n ≤ my_str의 길이
my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.
'''

def solution(my_str, n):
    answer = []
    while True:
        if len(my_str) > n:
            answer.append(my_str[:n])
            my_str = my_str[n:]
        else:
            answer.append(my_str)
            break
    return answer


# 입문 문제 - 공 던지기
# 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
# 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

'''
2 < numbers의 길이 < 100
0 < k < 1,000
numbers의 첫 번째와 마지막 번호는 실제로 바로 옆에 있습니다.
numbers는 1부터 시작하며 번호는 순서대로 올라갑니다.
'''

def solution(numbers, k):
    answer = 0

    num_len = len(numbers) + 2 * (k - 1)
    temp = num_len % len(numbers)
    answer = numbers[temp]
    return answer


# 입문 문제 - 캐릭터의 좌표
# 머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
# 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
# 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 
# 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
# [0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

'''
board은 [가로 크기, 세로 크기] 형태로 주어집니다.
board의 가로 크기와 세로 크기는 홀수입니다.
board의 크기를 벗어난 방향키 입력은 무시합니다.
0 ≤ keyinput의 길이 ≤ 50
1 ≤ board[0] ≤ 99
1 ≤ board[1] ≤ 99
keyinput은 항상 up, down, left, right만 주어집니다.
'''

def solution(keyinput, board):
    answer = [0,0]
    left_right = board[0]
    up_down = board[1]

    for i in keyinput:        
        if i == 'left':
            if answer[0] > -1 * (left_right // 2):
                answer[0] -= 1  
        elif i == 'right':
            if answer[0] < left_right // 2:
                answer[0] += 1
        elif i == 'up':
            if answer[1] < up_down // 2:
                answer[1] += 1 
        elif i == 'down':
            if answer[1] > -1 * (up_down // 2):
                answer[1] -= 1

    return answer



