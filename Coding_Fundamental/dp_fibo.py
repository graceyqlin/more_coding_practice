
def get_num(index):
	dp = [0] * (index + 1)
	dp[0] = 1
	dp[1] = 1
	for i in range(2, index):
		dp[i] = dp[i-1] + dp[i-2]

	return dp[-1]

index = 5

get_num(index)