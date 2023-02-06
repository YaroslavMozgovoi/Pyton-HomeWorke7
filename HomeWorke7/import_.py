def get():
    id = input("Введите : id ")
    name = input("Введите : имя ")
    surname = input("Введите : фамилию ")
    tel = input("Введите : номер телефона ")

    with open('file_HomeWork7.txt','a') as data:
        data.writelines(f" {id}, {name}, {surname}, {tel}\n")
        print("Данные заисались")



