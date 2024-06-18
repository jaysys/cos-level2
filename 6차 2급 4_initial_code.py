#다음과 같이 import를 사용할 수 있습니다.
import math

def _solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

def solution(cards):
    #여기에 코드를 작성해주세요. blue, red, black
    answer =0
    suma = 0
    count = [0 for _ in range(3)]
    print(count)
    for card in cards:
        if card[0] == "blue":
            count[0] += 1
        elif card[0] == "red":
            count[1] += 1
        elif card[0] == "black":
            count[2] += 1
        suma += int(card[1])
    print(count, suma)

    if count[0] == 3 or count[1] == 3 or count[2] == 3:
        answer = suma*3
    elif count[0] == 2 or count[1] == 2 or count[2] == 2:
        answer = suma*2
    else:
        answer = suma
    print(answer)
    return answer



#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")