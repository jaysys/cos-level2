#다음과 같이 import를 사용할 수 있습니다.
import math

def _solution(people):
    #여기에 코드를 작성해주세요.
    answer = [0 for _ in range(4)]
    return answer

def solution(people): ##이것도 오케!
    #여기에 코드를 작성해주세요.
    answer = [0 for _ in range(4)]
    print(answer)
    for i in people:
        if i < 95:
            answer[0] += 1
        elif i<100:
            answer[1] += 1
        elif i<105:
            answer[2] += 1
        elif i>=105:
            answer[3] += 1
    print(answer)
    return answer

def solution(people):
    answer = [0 for _ in range(4)]
    for p in people:
        if p < 95:
            answer[0] += 1
        elif p >= 95 and p < 100:
            answer[1] += 1
        elif p >= 100 and p < 105:
            answer[2] += 1
        elif p >= 105:
            answer[3] += 1
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")