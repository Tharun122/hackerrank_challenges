# Rod cutting
def rod_cutting(price: list[float], n: int):
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], price[j-1] + dp[i-j])
    return dp[n]

print("\nRod cutting")
prices = [100, 5, 20, 40, 10000]
rod_length = 4
max_revenue = rod_cutting(prices, rod_length)
print("Maximum revenue obtainable:", max_revenue)

# Coin change
def coin_change(coins: list[int], amount: int):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

print("\nCoin change")
coins = [1, 2, 3]
target_amount = 11
min_coins = coin_change(coins, target_amount)
if min_coins != -1:
  print("Minimum number of coins:", min_coins)
else:
  print("No solution possible with given denominations")

# Max sum of non-adjacent elements in an array

def max_sum_no_adjacent(arr):
    arrLength = len(arr)
    if arrLength == 0:
        return 0
    memo = []
    for i in range(arrLength):
        if i == 0:
            memo.append(arr[i])
        elif i == 1:
            memo.append(max(memo[0], arr[i]))
        else:
            temp = memo[1]
            memo[1] = max(memo[1], memo[0] + arr[i])
            memo[0] = temp
    return memo[len(memo)-1]

print(max_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
print(max_sum_no_adjacent([1]))
print(max_sum_no_adjacent([1, 10, 7]))

# No of ways to make change

def ways_to_make_change(denoms, amount):
    memo = [0 for _ in range(amount+1)]
    memo[0] = 1
    for d in denoms:
        if(d > amount):
            break
        for i in range(amount):
            a = i + 1
            if d > a:
                continue
            memo[a] = memo[a] + memo[a-d]
    return memo[amount]


print(ways_to_make_change([1,5,10,25], 126))

# Min coins for change
def min_coins_for_change(denoms, amount):
    memo = [-1 for _ in range(amount+1)]
    memo[0] = 0
    if amount == 0:
        return 0
    for d in denoms:
        for a in range(1, amount+1):
            if d <= a:
                if memo[a-d] == -1:
                    continue
                new_count = 1 + memo[a-d]
                memo[a] = new_count if memo[a] == -1 else min(new_count, memo[a])
    return memo[amount]
