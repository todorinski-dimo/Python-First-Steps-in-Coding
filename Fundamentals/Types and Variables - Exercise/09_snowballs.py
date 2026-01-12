snow_balls = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_score = 0
for _ in range(1, snow_balls +1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    score = (snowball_weight // snowball_time) ** snowball_quality
    if score > max_score:
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
        max_score = score

print(f"{max_snowball_weight} : {max_snowball_time} = {max_score} ({max_snowball_quality})")