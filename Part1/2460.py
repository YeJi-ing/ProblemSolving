# 지능형 기차 2

if __name__ == "__main__":
    current_num = 0    
    max_num = 0

    for i in range(1, 11): #1~10개의 역
        out_man, in_man = map(int, input().split())
        current_num = current_num - out_man
        current_num = current_num + in_man

        if current_num > max_num:
            max_num = current_num

    print(max_num)
