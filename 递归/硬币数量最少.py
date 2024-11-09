num = 63
coins = [1, 5, 10, 21, 25]  # 币值

zhao = []


def min_coins(coins, num):
    if num == 0:
        return 0
    for i in reversed(coins):
        if i <= num:
            zhao.append(i)
            return 1 + min_coins(coins, num - i)

def gaijin_digui(coins, num):
    pass


print(min_coins(coins, num))
print(zhao)
