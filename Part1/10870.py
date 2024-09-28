# 피보나치 수 5

if __name__ == "__main__":
    idx = int(input(""))
    
    k1 = 0
    k2 = 1
    num = 0

    if idx == 0:
        print(k1)
    elif idx == 1:
        print(k2)
    else:
        for i in range (0, idx-1):
            num = k1 + k2
            k1 = k2
            k2 = num
        print(num)
