def trib_calc(cycles: int) -> list:
    """takes a how many tribonacci numbers to generate; returns a list with the numbers"""
    value = [1]
    for _ in range(cycles - 1):
        value.append(sum(value[-3:]))
    return value


trib_cycles = int(input())
result_list = trib_calc(trib_cycles)
result_list = [str(item) for item in result_list]
print(" ".join(result_list))
