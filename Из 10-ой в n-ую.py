def translate_from_ten_to_n(number, system):
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = []

    while number != 0:
        end = number % system
        number //= system
        if end in [i for i in range(10)]:
            s.append(end)
        else:
            end -= 10
            end = eng_upper_alphabet[end]
            s.append(end)

    s = s[::-1]
    return s


print('-Здравствуйте, это прогам нужно для перевода числа из 10-ой системы в любую другую. И так какое ваше число?')
n = input('-')
while not n.isdigit():
    print('-Ваше число должно быть в десятичной системе счисления. Если вы этого еще не поняли, то вы ЕБЛАН. Так каково ваше чило?')
    n = input('-')
n = int(n)

print('-Хорошо теперь выбирете систему. Прога работает с системами от 2-ой до 35-ой')
sys = input('-')
while not sys.isdigit():
    print('-Ты еблан? Пиши систему нормально, то есть цифрами, уёба')
    sys = input('-')
sys = int(sys)

print('-Вот ваше число!', end = " ")
print(*translate_from_ten_to_n(n, sys), sep='')