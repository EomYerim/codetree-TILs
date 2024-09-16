import sys
input = sys.stdin.readline
from collections import Counter

N =int(input())
students=[input().rsplit() for i in range(N)]
result = {}
if N==1:
    print(students[0][0])
else:
    scores = Counter()
    for name, score in students:
        scores[name] += int(score)
#min이 여러개면 차순위, 차순위 개수도 여러개면 Tie, 
# 최소값 찾기
    min_value = min(scores.values())
    max_value = max(scores.values())
    if(min_value==max_value):
        print("Tie")
    # 최소값이 1개일때 
    else:
        result = Counter({k: v for k, v in scores.items() if v == min_value})
        if(len(result)==1):
            min_keys = [k for k, v in result.items() if v == min_value]
            print(min_keys[0])
        #최소값이 여러개일경우
        else:
            res = Counter({k: v for k, v in scores.items() if v > min_value})
            result_min_value = min(res.values())
            min_keys = [k for k, v in res.items() if v == result_min_value]

        # 최소값을 가진 키의 개수 확인
            if len(min_keys) > 1:
                print("Tie")
            else:
                print(min_keys[0])