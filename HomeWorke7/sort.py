def sort_id():
    with open('file_HomeWork7.txt',"r") as data:
        list = data.readlines()
        list_1 = []
        for lain in list:
            a = lain.split(",")
            print(a)
            list_1.append(a)
        list_1 = sorted(list_1, key = lambda x: x[0])
        string_ = " "
        for i in list_1:
            res = ",".join(i)
            string_ += res
        with open('file_HomeWork7.txt',"w") as data:
            data.write(string_)

