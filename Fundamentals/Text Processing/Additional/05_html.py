counter = 0
while True:
    string = input()
    if string == "end of comments":
        break
    elif counter == 0:
        print("<h1>\n", string, "\n</h1>")
    elif counter == 1:
        print("<article>\n", string, "\n</article>")
    elif counter > 1:
        print("<div>\n", string, "\n</div>")
    counter += 1
