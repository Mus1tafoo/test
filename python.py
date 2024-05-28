imena = []
nomera = []
uslugi = []
while True:
    primer1 = input("что хотите сделать:")
    if primer1 == "добавить":
        primer2 = input("Как вас зовут:")
        primer3 = input("Номер телефона:")
        imena.append(primer2)
        nomera.append(primer3)
    elif primer1 == "Услуга":
        primer4 = input("Какая услуга вас интерисует:")
        uslugi.append(primer4)
        pimer5 = ("Ваша заявка принета")
        print(pimer5)
    elif primer1 == "закрыть":
        break
    elif primer1 == "Показать список имен":
        print(imena)
    elif primer1 == "Показать список номеров":
        print(nomera)
    elif primer1 == "Показать список услуг":
        print(uslugi)