age = int(input())
message = "drink "
drinks_age_14 = "toddy"
drinks_age_18 = "coke"
drinks_age_21 = "beer"
drinks_age_rest = "whisky"

if age <= 14:
    print(message+drinks_age_14)
elif age <= 18:
    print(message+drinks_age_18)
elif age <= 21:
    print(message+drinks_age_21)
else:
    print(message+drinks_age_rest)


