# 약수 구하기

if __name__ == "__main__":
    N, K = map(int, input().split())

    list = []
    num  = 0
    for i in range(1, N+1):
        if N % i == 0:
            #print(i)
            list.append(i)
            num = num + 1
        
    result = 0
    if num < K:
        result = 0
    else:
        result = list[K-1]
    
    print(result)