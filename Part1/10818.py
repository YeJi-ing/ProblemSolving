# 최소, 최대
def find_min_max(Num, NumList):
    for i in range(0, Num):
        for j in range (i, Num):
            if NumList[i] > NumList[j]:
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp
    
    min = NumList[0]
    max = NumList[Num-1]

    return min, max

if __name__ == "__main__":
    num = int(input(""))
    NumList = [*map(int, input().split())]

    min, max = find_min_max(num, NumList)

    print(min, " ", max)