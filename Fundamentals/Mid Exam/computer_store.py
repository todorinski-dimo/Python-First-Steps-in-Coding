order_value = 0
tax = 0.2
discounted = 0.9

while True:
    cmd = input()
    if (cmd == "regular" or cmd == "special") and order_value > 0:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {order_value:.2f}$")
        print(f"Taxes: {(tax * order_value):.2f}$")
        print("-----------")
        if str(cmd) == "regular":
            print(f"Total price: {(order_value + tax * order_value):.2f}$")
        if str(cmd) == "special":
            print(f"Total price: {(discounted * (order_value + tax * order_value)):.2f}$")
        break
    elif (cmd == "regular" or cmd == "special") and order_value == 0:
        print("Invalid order!")
        break
    cmd = float(cmd)
    if cmd <= 0:
        print("Invalid price!")
    if cmd > 0:
        order_value += float(cmd)
