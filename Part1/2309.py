# 일곱 난쟁이
# 9명 중에 2명이 스파이인 경우의 수 = 9C2 = 72 / 2 = 36

if __name__ == "__main__":
    height = []
    x_man1 = 0
    x_man2 = 0

    # 입력 받기
    for i in range (0, 9): #0~8
       num = int(input())
       height.append(num)

    for i in range (0, 9):
        for j in range(i+1, 9): #8 8 이런거 없이
            # i번째와 j번째를 뺀 값 계산하여 100인지 확인
            total_heigh = 0
            for x in range (0, 9):
                if x != i and x != j:
                    total_heigh = total_heigh + height[x]

            if total_heigh == 100:
                x_man1, x_man2 = i, j

    # 스파이 제거, 한 인덱스 제거하면 나머지 인덱스 변경되므로 주의, 큰 인덱스부터 제거
    del height[x_man2]
    del height[x_man1]

    # 오름차순 정렬
    for i in range (0, 7): #0~6
        for j in range (i, 7):
            if height[i] > height[j]:
                temp = height[i]
                height[i] = height[j]
                height[j] = temp

    print(*height, sep='\n')