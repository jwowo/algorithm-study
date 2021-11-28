"""백준 1946번 신입사원 https://www.acmicpc.net/problem/1946"""
"""문제
최고만을 지향하는 대기업 진영 주식회사의 신규 사원 채용
1차 서류심사와 2차 면접시험으로 이루어진다.
최고의 인재들만 사원으로 선발하고 싶다.

그래서 진영 주식화사는 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중
적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칠을 세웠다.

즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면
A는 결코 선발되지 않는다.

T : 테스트 케이스의 개수 ( 1 <= T <= 20 )
N : 지원자의 숫자 ( 1 <= N <= 100,000 )

각각의 지원자의 서류 심사 성적, 면접 성적의 순위
두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다.
"""
"""


서류 전형은 오름차순했기때문에 더 볼 필요가 없다.
면접 등수가 이전 지원자보다 더 낮다면 회사는 그 사람을 채용하지 않을 것 이다. 

면접 등수에 대해서만 반복문으로 돌면서
현재 지원자와 다음 지원자의 면접 점수를 비교한다.
현재 지원자보다 다음 지원자의 면접 등수가 더 낮다면(등수가 클 때)
정답에 1을 더한다.
반복문을 돌면서 현재 지원자의 면접 점수를 다음 지원자의 면접 점수로 갱신해준다.

포인트는 굳이 이중 for문을 사용할 필요가 없었다.
"""

### max 값을 갱신하면서 푸는 방법
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []
    
    for _ in range(N):
        documents_rank, interview_rank = map(int, input().split())
        applicants.append((documents_rank, interview_rank))

    applicants.sort(key = lambda x : x[0])

    max_interview_rank = applicants[0][1]
    ans = 1

    for i in range(1, N):
        current_interview_rank = applicants[i][1]
        
        if max_interview_rank > current_interview_rank:
            ans += 1
            max_interview_rank = current_interview_rank

    print(ans)

"""min value를 이용한 풀이
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []
    
    for _ in range(N):
        documents_rank, interview_rank = map(int, input().split())
        applicants.append((documents_rank, interview_rank))

    applicants.sort(key = lambda x : x[0])

    min_interview_rank = applicants[0][1]
    ans = 0

    for i in range(1, N):
        current_interview_rank = applicants[i][1]
        
        if current_interview_rank > min_interview_rank:
            ans += 1
        else:
            min_interview_rank = current_interview_rank

    print(N - ans)
"""

"""처음 짠 시간 초과 코드
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []
    
    for _ in range(N):
        documents_rank, interview_rank = map(int, input().split())
        applicants.append((documents_rank, interview_rank))

    applicants.sort(key = lambda x : x[0])
    fail_applicants = set()

    for i in range(N):
        for j in range(i + 1, N):
            if j in fail_applicants:
                continue
            elif applicants[i][1] < applicants[j][1]:
                fail_applicants.add(j)
                
    print(N - len(fail_applicants))
"""