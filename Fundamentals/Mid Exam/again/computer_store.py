tax = 0.2
tax_value = 0
discount = 0.1
final_value_wt_tax = 0
final_value = 0

while True:
    cmd = input()
    if cmd == "special":
        final_value = final_value * (1 - discount)
        break
    elif cmd == "regular":
        break
    elif float(cmd) > 0:
        final_value_wt_tax += float(cmd)
        tax_value = final_value_wt_tax * tax
        final_value = final_value_wt_tax + tax_value
    else:
        print("Invalid price!")


if final_value > 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {final_value_wt_tax:.2f}$\n"
          f"Taxes: {tax_value:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_value:.2f}$")
else:
    print("Invalid order!")