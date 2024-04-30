def min_distance_to_avoid_obstacles(n, obstacles):
    import sys
    # dp[y][0]은 y행의 왼쪽 끝에서 최소 거리, dp[y][1]은 y행의 오른쪽 끝에서 최소 거리
    dp = [[sys.maxsize, sys.maxsize] for _ in range(n + 2)]
    # 초기 위치 설정
    dp[0][0] = dp[0][1] = 0

    # y = 1부터 n까지 각 장애물 처리
    for i in range(1, n + 1):
        left, right = obstacles[i - 1]
        # 해당 장애물을 둘러서 이동하는 비용 계산
        if i > 1:
            # 왼쪽 끝 도달 최소 비용
            dp[i][0] = min(dp[i][0], dp[i-1][0] + abs(obstacles[i-2][0] - left) + 1)
            dp[i][0] = min(dp[i][0], dp[i-1][1] + abs(obstacles[i-2][1] - left) + 1)
            # 오른쪽 끝 도달 최소 비용
            dp[i][1] = min(dp[i][1], dp[i-1][0] + abs(obstacles[i-2][0] - right) + 1)
            dp[i][1] = min(dp[i][1], dp[i-1][1] + abs(obstacles[i-2][1] - right) + 1)
        else:
            # 첫 장애물인 경우, 원점에서 시작
            dp[i][0] = abs(left) + 1
            dp[i][1] = abs(right) + 1

    # 마지막 장애물을 지난 후 도착 지점까지의 이동 거리
    dp[n+1][0] = min(dp[n][0] + abs(obstacles[n-1][0]), dp[n][1] + abs(obstacles[n-1][1])) + 1
    dp[n+1][1] = dp[n+1][0]  # 도착 지점은 x = 0에서만 계산

    return dp[n+1][0]

# 예제 입력 처리



n = int(input())  # 장애물의 개수
obstacles = []    # 장애물 정보를 담을 리스트

# 장애물 정보 입력받기
for _ in range(n):
    left, right = map(int, input().split())
    obstacles.append((left, right))
print(min_distance_to_avoid_obstacles(n, obstacles))
