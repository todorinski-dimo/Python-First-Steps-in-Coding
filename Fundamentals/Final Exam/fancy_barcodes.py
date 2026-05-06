import re
regex = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    product_group = ""
    barcode = input()
    match = re.match(regex, barcode)
    if match:
        sub_barcode = match.group(1)
    else:
        print("Invalid barcode")
        continue
    for char in sub_barcode:
        if char.isnumeric():
            product_group += char
    if len(product_group) == 0:
        print("Product group: 00")
    else:
        print(f"Product group: {product_group}")