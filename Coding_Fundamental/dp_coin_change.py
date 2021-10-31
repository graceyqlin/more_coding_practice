# you have coins 1, 5, 10, 25. how many ways can you combine the coins to get total dollar of n?


def get_ways(dollar, coins):

	dp = [0] * (dollar + 1)

	dp[0] = 1

	dp[1] = 1

	dp[2] = 1

	for d in range(1, dollar + 1):

		for coin in coins:

			mod = d // coin

			diff = d - coin

			if mod == 0 and dp[diff] >0:

				dp[d] = min(dp[diff]


	return dp[-1]

coins = [1, 5, 10, 25]

dollar = 3

print(get_ways(dollar, coins))



