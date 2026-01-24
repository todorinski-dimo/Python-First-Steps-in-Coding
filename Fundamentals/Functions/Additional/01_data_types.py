def method_overload(datatype: str, data) -> int or float or str:
    if datatype == "int":
        res = int(data)
        return res * 2
    if datatype == "real":
        res = float(data)
        return f"{res * 1.5:.2f}"
    if datatype == "string":
        return f"${data}$"


input_type = input()
input_input = input()
print(method_overload(input_type, input_input))
