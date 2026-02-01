# https://alpha.judge.softuni.org/contests/02-programming-fundamentals-mid-exam/2474/practice

from math import ceil

emplo_1_st_hour = int(input())
emplo_2_st_hour = int(input())
emplo_3_st_hour = int(input())
st_number = int(input())

emplo_all_st_hour = emplo_1_st_hour + emplo_2_st_hour + emplo_3_st_hour
# print(emplo_all_st_hour)
working_time_needed = ceil(st_number / emplo_all_st_hour)
# print(working_time_needed)
rest_needed = working_time_needed // 3
# print(rest_needed)
total = working_time_needed + rest_needed
# print(total)

print(f"Time needed: {total}h.")
