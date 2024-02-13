def get_chips_count():
    s = int(input("Сколько каллорий вы хотите набрать?: "))
    kkal_to100 = 510
    weight_one = 140
    kkal_in_one = kkal_to100 * weight_one // 100
    one_gramm_kkal = kkal_in_one / weight_one
    itog = s / one_gramm_kkal
    part_of_box = itog / weight_one
    print(f"Вам необходимо съесть {itog.__round__(2)} грамм")
    print(f"Что равняется {part_of_box.__round__(2)} Пачки")
get_chips_count()