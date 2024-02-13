def get_count_dumplings():
    ves = 385
    count_d = 11
    kkal = 231
    kkalvsego = kkal * ves // 100
    kkalone = kkalvsego / count_d
    count = int(input("Введите количество дамплингов: "))
    list = []

    for i in range(1, count + 1):
        if count % i == 0 and i != 1 and i != count:
            list.append([f"Количество дамплингов в порции - {i} / Каллорий в порции - {kkalone.__round__() * i} / Количество порций - {int(count / i)}"])
    print("Варианты потребления:")
    for i in list:
        print(*i)

get_count_dumplings()