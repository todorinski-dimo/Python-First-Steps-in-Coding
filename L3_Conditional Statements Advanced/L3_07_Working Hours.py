hour = int(input())
weekday = input()

if (10 <= hour <= 18) and (weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday
                           == "Thursday" or weekday == "Friday" or weekday == "Saturday"):
    print("open")
else:
    print("closed")
