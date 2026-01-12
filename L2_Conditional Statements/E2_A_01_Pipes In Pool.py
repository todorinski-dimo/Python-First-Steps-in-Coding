pool_volume = int(input())
pipe1_debit_per_hour = int(input())
pipe2_debit_per_hour = int(input())
hours_of_return = float(input())

filled_volume = hours_of_return * (pipe1_debit_per_hour + pipe2_debit_per_hour)
percent_from_pool = (filled_volume / pool_volume) * 100
percent_pipe1 = ((hours_of_return * pipe1_debit_per_hour) / filled_volume) * 100
percent_pipe2 = ((hours_of_return * pipe2_debit_per_hour) / filled_volume) * 100
overflow = filled_volume - pool_volume

if filled_volume <= pool_volume:
    print(f"The pool is {percent_from_pool:.02f}% full. Pipe 1: {percent_pipe1:.02f}%. Pipe 2: {percent_pipe2:.02f}%.")
else:
    print(f"For {hours_of_return:.02f} hours the pool overflows with {overflow:.02f} liters.")