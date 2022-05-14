print("Добро пожаловать в числовую угадайку")
a, b = input("Для того, чтобы сыграть, выберете нижний предел: "), input("и верхний предел: ")

count = 0
count_fail = 0
count_stupid = 0

def do_I_want_play_again(s):
    while True:
        if s in ["Да", "да", "ДА", "дА"]:
            a, b = input("Для того, чтобы сыграть, выберете нижний предел: "), input("и верхний предел: ")

            count = 0
            count_fail = 0
            count_stupid = 0

            while is_valid(a) == False or is_valid(b) == False:
                count_stupid += 1
                print("Давайте выберем натуральные числа.")
                a, b = input("Выберете нижний предел: "), input("и верхний предел: ")

            a, b = int(a), int(b)
            import random
            num = random.randint(a, b)

            n = input("Я загадала число. Угодайте его: ")

            is_right_num(n, num)

        elif s in ["Нет", "нЕт", "неТ", "НЕт", "нЕТ", "НеТ", "нет", "НЕТ"]:
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
        else:
            s = input('Вам следует напистаь "да" или "нет", а не что-либо ещё. Вы выбираете: ')

def is_valid(s):
    if s.isdigit(): return True
    else: return False

def how_many_count_need(a, b):
    count = 0
    c = b - a + 1
    while c >= 1:
        c /= 2
        count +=1
    return count

def do_you_need_help(s):
    if s in ["Да", "да", "ДА", "дА"]:
        kock = how_many_count_need(a, b)
        print("Есть алгоритм победы в числовой угадайке: вам просто нужно делить имеющийся отрезок в два раза")
        print("В вашем случае нужно найти кол-во чисел между нижним и верхним пределом, а потом поделить это кол-во на 2")
        print('Далее необходимо действовать относительно ответа программы, если прога говорит, - "Это слишком много", - значит ваше число теперь верхний предел')
        print('Если прога написала, - "Это слишком мало", - значит ваше число теперь нижний предел')
        print("Кста, в вашем случае для точной победы нужно", kock, "попыток")
        print("Хихихихихихихих")

def is_right_num(n, num):
    global count
    global count_stupid
    global count_fail

    while num:
        count += 1
        if is_valid(n) == True and count <= how_many_count_need(a, b):
            n = int(n)
            if n < a or n > b:
                n = input("Вам следует вебрать число в пределах, выбранных ранее: ")
                count_stupid +=1
            elif n > num:
                n = input("Слишком много, попробуйте еще раз: ")
                count_fail += 1

            elif n < num:
                n = input("Слишком мало, попробуйте еще раз: ")
                count_fail += 1

            elif n == num:
                print("Вы угадали, поздравляем!", "Число:", num, "| Кол-во попыток:", count, "Из них неудачных:",
                      count_fail,
                      end=",")
                print(" а идитиоских:", count_stupid)
                otvet = input('Вы хотели бы сыграть еще раз? "Да" или "нет": ')
                do_I_want_play_again(otvet)
                break

        elif is_valid(n) == True and count > how_many_count_need(a, b):
            n = int(n)
            if n < a or n > b:
                n = input("Вам следует вебрать число в пределах, выбранных ранее: ")
                count_stupid +=1

            elif n > num:
                n = input("Слишком много, попробуйте еще раз: ")
                count_fail += 1
                s = input('Вы хотели бы узнать, - "Как решать подобные угодаки", - тогда напишите "да": ')
                do_you_need_help(s)

            elif n < num:
                n = input("Слишком мало, попробуйте еще раз: ")
                count_fail += 1
                s = input('Вы хотели бы узнать, - "Как решать подобные угодаки", - тогда напишите "да": ')
                do_you_need_help(s)

            elif n == num:
                print("Вы угадали, поздравляем!", "Число:", num, "| Кол-во попыток:", count, "Из них неудачных:",
                      count_fail,
                      end=",")
                print(" а идитиоских:", count_stupid)
                otvet = input('Вы хотели бы сыграть еще раз? "Да" или "нет": ')
                do_I_want_play_again(otvet)
                break


        else:
            n = input("А может быть все-таки введем целое число от верхнего до нижнего предела?: ")
            count_stupid += 1

while is_valid(a) == False or is_valid(b) == False:
    count_stupid += 1
    print("Давайте выберем натуральные числа.")
    a, b = input("Выберете нижний предел: "), input("и верхний предел: ")

a, b = int(a), int(b)
import random
num = random.randint(a, b)

n = input("Я загадала число. Угодайте его: ")


is_right_num(n, num)