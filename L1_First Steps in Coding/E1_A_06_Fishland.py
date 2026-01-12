fish1_price = float(input())
fish2_price = float(input())
fish3_weight = float(input())
fish4_weight = float(input())
fish5_weight = int(input())

fish3_price = fish1_price * 1.6
fish4_price = fish2_price * 1.8
fish5_price = 7.5

print(f"{fish3_price * fish3_weight + fish4_price * fish4_weight + fish5_price * fish5_weight:.02f}")

