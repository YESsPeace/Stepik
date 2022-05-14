rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
russian = rus_lower_alphabet + rus_upper_alphabet

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
english = eng_upper_alphabet + eng_lower_alphabet

#Функции дешифрование и шифрования

def chef_rus(s, key):
    global rus_upper_alphabet, rus_lower_alphabet

    chef_s = ''

    for i in s:
        if i in rus_lower_alphabet or i in rus_upper_alphabet:
            if i == i.lower():
                n = rus_lower_alphabet.find(i)
                n = (n + key) % 32
                i = rus_lower_alphabet[n]
                chef_s += str(i)


            elif i == i.upper():
                n = rus_upper_alphabet.find(i)
                n = (n + key) % 32
                i = rus_upper_alphabet[n]
                chef_s += str(i)


        else:
            chef_s += str(i)

    return chef_s


def dechef_rus(s, key):
    global rus_upper_alphabet, rus_lower_alphabet

    dechef_s = ""

    for i in s:
        if i in rus_lower_alphabet or i in rus_upper_alphabet:
            if i == i.lower():
                n = rus_lower_alphabet.find(i)
                n = (n - key) % 32
                i = rus_lower_alphabet[n]
                dechef_s += str(i)


            elif i == i.upper():
                n = rus_upper_alphabet.find(i)
                n = (n - key) % 32
                i = rus_upper_alphabet[n]
                dechef_s += str(i)


        else:
            dechef_s += str(i)

    return dechef_s


def chef_eng(s, key):
    global eng_lower_alphabet, eng_upper_alphabet

    chef_s = ""

    for i in s:
        if i in eng_lower_alphabet or i in eng_upper_alphabet:
            if i == i.lower():
                n = eng_lower_alphabet.find(i)
                n = (n + key) % 26
                i = eng_lower_alphabet[n]
                chef_s += str(i)


            elif i == i.upper():
                n = eng_upper_alphabet.find(i)
                n = (n + key) % 26
                i = eng_upper_alphabet[n]
                chef_s += str(i)


        else:
            chef_s += str(i)

    return chef_s


def dechef_eng(s, key):
    global eng_lower_alphabet, eng_upper_alphabet

    dechef_s = ""

    for i in s:
        if i in eng_lower_alphabet or i in eng_upper_alphabet:
            if i == i.lower():
                n = eng_lower_alphabet.find(i)
                n = (n - key) % 26
                i = eng_lower_alphabet[n]
                dechef_s += str(i)


            elif i == i.upper():
                n = eng_upper_alphabet.find(i)
                n = (n - key) % 26
                i = eng_upper_alphabet[n]
                dechef_s += str(i)


        else:
            dechef_s += str(i)

    return dechef_s

#Функции дешифрование и шифрования

def yes_or_no(s):
    while True:
        if s in ["Да", "ДА", "да", "дА"]:
            return True
        elif s in ["Нет", "НЕт", "НЕТ", "нЕт", "нЕТ", "НеТ", "НЕТ", "нет", "неТ"]:
            return False
        else:
            print('-Ответ должен быть "Да" или "Нет"')
            s = input("-")
            continue
#Функция опр. "Да" или "Нет". Выдаёт True или False


print("-Приветствую вас, вы попали в программу, которая поможет вам зашифровать и дишифровать сообщение,"
      "при шифровании которго использовался шифр Цезаря. Нужно лишь само сообщение и ключ")

print("-Введите сообщение")
s = input("-")

print("-Вы знаете ключ?") #Это нужно для зиапазона ключей
know_key = input("-")
know_key = yes_or_no(know_key)

#Если ключ известен, узнаем его значение
if know_key == True:
    print("-Введите ключ")
    key = input("-")
    while not key.isdigit(): #Проверка числа Ключа
        print("-Давайте всё-таки число")
        key = input("-")
    key = int(key)

#Если ключ не известен, узнаем его диапазон
else:
    print("-Введите начало диапазона")
    start = input("-")
    while not start.isdigit(): #Проверка числа начала диапазона
        print("-Давайте всё-таки число")
        start = input("-")
    start = int(start)

    print("-Введите конец диапазона")
    end = input("-")
    while not end.isdigit(): #Проверка числа конца диапазона
        print("-Давайте всё-таки число")
        end = input("-")
    end = int(end)

print('-Вы хотите дешифровать сообщение? "Да" или "Нет"?')
whats_need = input("-")
whats_need = yes_or_no(whats_need)  #Возвращает True или False

#Если ключ известен - Шифруем или Дешифруем
if know_key == True:
    if whats_need == True:
        output_s = ''
        for i in s: #Должен сканить отдельно каждый символ | Дешифрование
            if i in russian:
                a = dechef_rus(i, key)
                output_s += a
            elif i in english:
                a = dechef_eng(i, key)
                output_s += a
            else:
                output_s += i
        print("-Вот сообщение")
        print(output_s)

    else:
        print("-Хорошо, значит - шифруем", end=". ")
        output_s = ''
        for i in s: #Должен сканить отдельно каждый символ | Шифрование
            if i in russian:
                a = chef_rus(i, key)
                output_s += a
            elif i in english:
                a = chef_eng(i, key)
                output_s += a
            else:
                output_s += i
        print("Вот сообщение")
        print(output_s)

#Если ключ не известен - Дешифруем
else: #Если мы знаем только диапазон ключа
    if start > end:
        start, end = end, start

    for key in range(start, end + 1):
        if whats_need == True:
            output_s = ''
            for i in s:  # Должен сканить отдельно каждый символ | Дешифрование
                if i in russian:
                    a = dechef_rus(i, key)
                    output_s += a
                elif i in english:
                    a = dechef_eng(i, key)
                    output_s += a
                else:
                    output_s += i
            print("-Вот сообщение с ключом:", key)
            print(output_s)
            print()
