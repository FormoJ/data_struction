# 动态规划解法
def dp_my_solution(list1, much, max):
    for cents in range(much + 1):
        min_coins = cents  # 初始化动态规划列表
        for j in [c for c in list1 if c <= min_coins]:
            if max[cents - j] + 1 < min_coins:  # 如果下一步加上这一步的硬币数还小于上面动态规划存储的硬币数，那么就存储更小的值
                min_coins = max[cents - j] + 1
        max[cents] = min_coins
    return max[cents]


# 最多找零63个硬币
# print(dp_make_change([1, 5, 10, 21, 25], 63, [0] * 64))
print(dp_my_solution([1, 5, 10, 21, 25], 63, [0] * 64))
