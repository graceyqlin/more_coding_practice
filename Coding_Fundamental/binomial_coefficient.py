# binomial coefficient for dymanic programming

# Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). 
# For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.

def get_binomial(n, k):
	dp = [[1] * (k+1) for _ in range(n+1)]

	for row in range(1, n+1):
		for col in range(1, k+1):
			if row > col:
				dp[row][col] = dp[row-1][col-1]  + dp[row-1][col]

	print(dp)
	return dp[-1][-1]

n = 5
k = 2

print(get_binomial(n, k))