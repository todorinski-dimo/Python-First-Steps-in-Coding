nonworking_days = int(input())
max_playtime = 30000
working_day_playtime = 63
nonworking_day_playtime = 127
year_days = 365
hours_in_day = 24

working_days = year_days - nonworking_days
total_playtime = working_days * working_day_playtime + nonworking_days * nonworking_day_playtime
delta = abs(max_playtime - total_playtime)
delta_hours = delta // 60
delta_minutes = delta - (delta_hours * 60)

if max_playtime > total_playtime:
    print("Tom sleeps well")
    print(f"{delta_hours} hours and {delta_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{delta_hours} hours and {delta_minutes} minutes more for play")
