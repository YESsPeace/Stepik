print('-Введите ваше число')
num = input('-')    #Число

print('-Хорошо, теперь введите систему счисления')
sys_num = input('-')
while not sys_num.isdigit():
    print('-Простите, но мы работаем только с числовыми системами счисления')
    sys_num = input('-')
sys_num = int(sys_num) #Приняли и int систему счисления

def translate_number(number, system):
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    l = len(number)
    teny_number = 0

    for i in number:
        l -=1

        if i in eng_upper_alphabet:
            i = eng_upper_alphabet.find(i)
            i += 10
            teny_number = teny_number + (i * system ** l)

        else:
            i = int(i)
            teny_number = teny_number + (i * system**l)

    return teny_number

num = translate_number(num, sys_num)

print('-Вот ваше число в десятичной системе -', num)