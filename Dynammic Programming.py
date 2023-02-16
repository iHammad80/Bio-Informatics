def can_interweave(s, patterns):
    n = len(patterns)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if s.endswith(patterns[i]):
            dp[i][i] = 1
    
    for i in range(n):
        for j in range(i+1, n):
            if s.endswith(patterns[i] + patterns[j]):
                dp[i][j] = 1
            elif s.endswith(patterns[j] + patterns[i]):
                dp[i][j] = 1
            elif (s.endswith(patterns[i]) and dp[i][j-1]) or (s.endswith(patterns[j]) and dp[i+1][j]):
                dp[i][j] = 1
    return dp

s = "GACCACGGTT"
patterns = ["ACAG", "GT", "CCG"]
print(can_interweave(s, patterns))
