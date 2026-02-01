# https://alpha.judge.softuni.org/contests/02-programming-fundamentals-mid-exam/2474/practice

emplo_1_st_hour = int(input())
emplo_2_st_hour = int(input())
emplo_3_st_hour = int(input())
st_number = int(input())
done_st = 0
hours_worked = 0
hours_break = 0

not_done = True
emplo_all_st_hour = emplo_1_st_hour + emplo_2_st_hour + emplo_3_st_hour

while not_done:
    done_st += emplo_all_st_hour
    hours_worked += 1
    if done_st >= st_number:
        not_done = False
        break
    if hours_worked % 3 == 0:
        hours_break += 1

print(f"Time needed: {hours_worked + hours_break}h.")
