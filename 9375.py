def count_combinations(test_cases):
    results = []
    
    for _ in range(test_cases):
        # 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)
        n = int(input())
        if n == 0:
            results.append(0)
        else:
            clothes = {}
            
            for _ in range(n):
                name, category = input().split()
                if category not in clothes:
                    clothes[category] = 0
                clothes[category] += 1
            
            # 각 의상 종류에 대해 조합 계산
            combinations = 1
            for count in clothes.values():
                combinations *= (count + 1)  # 해당 종류를 선택하지 않는 경우 포함
            
            # 다 선택하지 않은 경우 빼기
            results.append(combinations - 1) 
        
    return results

if __name__ == "__main__":
    # 입력 받기
    test_cases = int(input())
    results = count_combinations(test_cases)

    for result in results:
        print(result)
