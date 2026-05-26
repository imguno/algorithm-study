
def solution(triangle):
    memo = [[None] * len(row) for row in triangle]

    def dp(i, j):
        if i == len(triangle) - 1:
            return triangle[i][j]

        if memo[i][j] is not None:
            return memo[i][j]

        left = dp(i+1, j)
        right = dp(i+1, j+1)
        memo[i][j] = triangle[i][j] + max(left, right)
        return memo[i][j]

    return dp(0, 0)

if __name__ == "__main__":
	triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
	print(solution(triangle) == 30)

