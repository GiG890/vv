fp="C:/Users\TECNO\Documents\Pyt/files/example.txt"
with open(fp, "x") as file:
    file.write("I\nlive\ncakes")
def g (mode):
    try:
        if mode == "ob":
            with open(fp, "r") as file:
                content=file.read()
                print(content)
        elif mode =="sp":
            with open(fp, "r") as file:
                for line in file:
                    print(line[:-1])
    exept FileExistsError:
    print(" Такой файл уже есть")

g(input())