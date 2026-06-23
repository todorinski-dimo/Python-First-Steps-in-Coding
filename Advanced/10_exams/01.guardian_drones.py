from collections import deque

mechanical_parts = list(map(int, input().split()))
power_cells = deque(list(map(int, input().split())))

activation_power ={
    100:"Sentinel-X",
    85:"Viper-MKII",
    75:"Aegis-7",
    65:"Striker-R",
    55:"Titan-Core"
}

activated_drones = []

while mechanical_parts and power_cells and len(activated_drones) < 5:
    total_activation_power = mechanical_parts[-1] + power_cells[0]
    if (total_activation_power in activation_power) and (activation_power[total_activation_power] not in activated_drones):
        activated_drones.append(activation_power[total_activation_power])
        mechanical_parts.pop()
        power_cells.popleft()
    else:
        for energy, name in activation_power.items():
            if energy < total_activation_power and (name not in activated_drones):
                activated_drones.append(name)
                mechanical_parts.pop()
                power_cells[0] -= 30
                if power_cells[0] <= 0:
                    power_cells.popleft()
                else:
                    power_cells.rotate(-1)
                break
        else:
            mechanical_parts.pop()
            power_cells[0] -= 1
            if power_cells[0] <= 0:
                power_cells.popleft()
            else:
                power_cells.rotate(-1)

if len(activated_drones) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
if len(activated_drones) < 5:
    print("Mission Failed! Some drones were not built.")
if activated_drones:
    print(f"Assembled Drones: {', '.join(activated_drones)}")
if mechanical_parts:
    mechanical_parts =  mechanical_parts[::-1]
    print(f"Mechanical Parts: {', '.join(map(str, mechanical_parts))}")
if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")


