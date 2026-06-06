from collections import deque

def time_to_seconds(t_time:list) -> int:
    return t_time[2] + t_time[1]*60 + t_time[0]*3600

def seconds_to_time(sec:int) -> str:
    time_sec = sec % (24 * 3600)
    time = list()
    time.append(time_sec // 3600)
    time_sec -= time[0] * 3600
    time.append(time_sec // 60)
    time_sec -= time[1] * 60
    time.append(time_sec)
    return f"{time[0]:02}:{time[1]:02}:{time[2]:02}"


input_robots = input().split(";")
robots_data = {}
for robot in input_robots:
    name, service_time = robot.split("-")
    robots_data[name] = {"srv_time": int(service_time), "working_on": "", "working_until": 0}
# print(robots_data)

start_time = [int(item) for item in input().split(":")]
tik = time_to_seconds(start_time)
products = deque()
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    tik += 1
    product = products.popleft()
    assignment = False
    for name in robots_data.keys():
        if tik >= robots_data[name]["working_until"]:
            robots_data[name]["working_on"] = product
            robots_data[name]["working_until"] = tik + robots_data[name]["srv_time"]
            print(f"{name} - {robots_data[name]['working_on']} [{seconds_to_time(tik)}]")
            assignment = True
            break

    if not assignment:
        products.append(product)
