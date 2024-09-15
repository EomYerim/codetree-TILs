import sys
input = sys.stdin.readline
N =int(input())
stdents=[input().rsplit() for i in range(N)]
result = {}
if N==1:
    print(stdents[0][0])
else:
    for k, v in stdents:
        result[k] = result.get(k, 0) + int(v)
    scores = sorted(list(result.values()),reverse=False) #점수들 기준 check
    if(scores.count(scores[1])==N-1) :
        print("Tie")
    else:
        # 그 다음으로 낮은 학생 출력
        if scores.count(scores[0])>1:
                remove_set={scores[0]}
                scores = [i for i in scores if i not in remove_set]
        for key, value in result.items():
            if value ==scores[0]:
                if scores.count(scores[0])==1: 
                    print(key)
                else:
                    print("Tie")