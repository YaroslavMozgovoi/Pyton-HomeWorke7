import import_ as i
import export as e
import sort as s

def action():
    while True:
        do = input("Что сделать ? Записать  1. Прочесть  2. Сортировка по id 3. Выход 4.")
        if do == "1":
            i.get()
        elif do == "2":
            do_1 = input("Что прочесть?  Всё 1. Имя и Фамилии 2.")
            if do_1 == "1":
                e.read()
            elif do_1 == "2":
                e.name_famali()
        elif do == "3":
            s.sort_id()
            print("Сортировка произведина")
        elif do == "4":
            break
        else :
            print("Неправильный запрос")
