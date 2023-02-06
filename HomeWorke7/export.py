def read():
    with open('file_HomeWork7.txt',"r") as data:
        for line in data:
            print(line)
        data.close()


def name_famali():
    with open('file_HomeWork7.txt',"r") as data:
        list = [line for line in data]
        list_1 = []
        for i in range(len(list)):
            list_1.append(list[i].split())
            print(list_1[i][1],list_1[i][2])
