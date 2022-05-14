digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation= ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_']

chars = ''
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

def password_creat(len, digit, big, small, another, not_alone):
    global digits, lowercase_letters, uppercase_letters, punctuation
    from random import shuffle, choice, randint

    password = ''

    if not_alone:
        digits = [i for i in digits if not i in '01']
        lowercase_letters = [i for i in lowercase_letters if not i in 'ilo']
        uppercase_letters = [i for i in uppercase_letters if not i in 'LO']

    lst_of_lsts = []
    if digit: lst_of_lsts.extend(digits)
    if big: lst_of_lsts.extend(lowercase_letters)
    if small: lst_of_lsts.extend(uppercase_letters)
    if another: lst_of_lsts.extend(punctuation)
    shuffle(lst_of_lsts)
    lst_of_lsts = lst_of_lsts[0: len]
    for i in lst_of_lsts: password += i

    return password


print("Добро пожаловать в генератор паролей *Ваши данные - не сохраняются*")
print()
print("-Сколько паролей нужно? (число)")
n = input("-")
while not n.isdigit():
    print("-Давайте выберем число")
    n = input("-")
n = int(n)

for _ in range(n):
    print('-Какова длина пароля')
    l = input("-")

    while not l.isdigit():
        print("-Давайте выберем число")
        l = input("-")
    l = int(l)

    print('-Включать ли цифры "0123456789"? "Да" или "Нет"?')
    digit = input("-")
    digit = yes_or_no(digit)

    print('-Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? "Да" или "Нет"?')
    big = input("-")
    big = yes_or_no(big)

    print('-Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? "Да" или "Нет"?')
    small = input("-")
    small = yes_or_no(small)

    print('-Включать ли символы "!#$%&*+-=?@^_"? "Да" или "Нет"?')
    another = input("-")
    another = yes_or_no(another)

    print('-Исключать ли неоднозначные символы "il1Lo0O"? "Да" или "Нет"?')
    not_alone = input("-")
    not_alone = yes_or_no(not_alone)

    password = password_creat(l, digit, big, small, another, not_alone)
    print("-Вот ваш пароль:", password)

print()
print("Спасибо, что повспользовались генератором паролей от Дами Рэр Назарова")