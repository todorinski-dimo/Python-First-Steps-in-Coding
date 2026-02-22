a = 3.14
print(a)
#str()
str_a = str(a)
print("string a:", str_a)
#split()
str_split = str_a.split(".")
print("split by .:",str_split)
#reverse
str_reverse = str_a[::-1]
print("reverse str_a:", str_reverse)
# concat
b = "abc"
print("concat str_a + b:",str_a + " " + b)
#multiply
print("multiply b * 40:", b * 40)
#----------
string1 = "12345"
string2 = "12345 "
print("isdigit() of '12345' =", string1.isdigit())
print("isdigit() of '12345 ' =", string2.isdigit())
# print(isdigit(string1))
# print(isdigit(string2))
string3 = "HELLO"
string4 = "hello"
print("lower() of HELLO =", string3.lower())
print("upper() of hello =", string4.upper())
print("capitalize() of hello =", string4.capitalize())
print("endswith('lo') of hello =", string4.endswith("lo"))
print("startswith('he') of hello =", string4.startswith("he"))
string5 = "Hello World"
string6 = "hello2323"
print("find('l') of hello world =", string5.find("l"))
print("find('q') of hello world =", string5.find("q"))
print("index('o') of hello world =", string5.index("o"))
#print("index('q') of hello world =", string5.index("q"))
print("isalnum() of hello world =", string5.isalnum())
print("isalnum() of hello2323 =", string6.isalnum())
string7 = "  Hello  "
print("rstrip() of '  Hello  ' =", string7.rstrip())
print("lstrip() of '  Hello  ' =", string7.lstrip())
print("strip() of '  Hello  ' =", string7.strip())

string101 = "######"
string111 = "cccc######"
print("find ###### in ccccc#####", string111.find(string101))



