import numpy as np
def minDistance(word1, word2):
	"""
	:type word1: str
	:type word2: str
	:rtype: int
	"""
	m,n = len(word1),len(word2)

	dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

	for i in range(1,m+1):
		dp[i][0] = i
	for j in range(1,n+1):
		dp[0][j] = j

	for i in range(1,m+1):
		for j in range(1,n+1):
			if word1[i-1] == word2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
	print(np.array(dp))
	return dp[m][n]





if __name__ == '__main__':
	word1 = 'intention'
	word2 = 'execution'

	res = minDistance(word1,word2)

	print(res)

