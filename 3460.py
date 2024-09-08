
def Calculate(hex):
    RestList = []
    quot = hex

    # 10진수를 2진수로 변환하여 RestList에 저장
    while True:
        if quot == 1: # 맨 끝
            RestList.append(1)
            break
        elif quot == 0: # 맨 끝
            RestList.append(0)
            break
        else:
            temp = quot
            quot = quot // 2  # 몫
            rest = temp % 2   #나머지
            RestList.append(rest)
    
    # 1의 index 출력
    for i in range (0, len(RestList)):
        if RestList[i] == 1:
            print(i, end=' ')


if __name__ == "__main__":
    
    T = int(input(""))

    for _ in range(T):
        n = int(input(""))
        Calculate(n)
