def choose_coin(coins, target):
    coins.sort(reverse=True)
    used_coins = {}
    for coin in coins:
        if coin not in used_coins:
            used_coins[coin] = 0
        used_coins[coin] = target // coin
        target = target % coin
    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"
        for k, v in used_coins.items():
            if v == 0:
                continue
            else:
                result += f"{v} coin(s) with value {k}\n"
        return result

coins_list = [int(x) for x in input().split(", ")]
target_sum = int(input())

print(choose_coin(coins_list, target_sum))
