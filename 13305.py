
# 시작 지역의 가격으로 도착 지역까지 주유 가격 계산
def CalculateCost(RegionNum, RegionDistance, RegionCost, StartRegionNum, ArrvieReigionNum):
    cost = 0

    for i in range (StartRegionNum, ArrvieReigionNum):
        #print(i, " : ", cost)
        cost = cost + (RegionDistance[i] * RegionCost[StartRegionNum])
    
    return cost

if __name__ == "__main__":
    # 입력 받기
    RegionNum = int(input(""))
    RegionDistance = [*map(int , input().split())]
    RegionCost = [*map(int, input().split())]

    # 총 주유 가격
    cost = 0

    start_index = 0
    end_index = 0
    while start_index != RegionNum-1: # 3이면 0 1 2 
        min_cost = RegionCost[start_index]
        for j in range (start_index, RegionNum):
            if min_cost > RegionCost[j]:
                min_cost = RegionCost[j]
                end_index = j
                break
            if j + 1 == RegionNum:
                end_index = j
        cost = cost + CalculateCost(RegionNum, RegionDistance, RegionCost, start_index, end_index)
        #print("start: ", start_index, " end: ", end_index, "cost: ", cost)
        start_index = end_index

    print(cost)