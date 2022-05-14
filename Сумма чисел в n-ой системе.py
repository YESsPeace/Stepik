print('-Введите сумму чисел')
sum_num = input('-')

print('-Введите кол-во чисел, которые составляют эту сумму')

nums = input('-')
while not nums.isdigit():
    print('-Давайте всё-так число')
    nums = input('-')
nums = int(nums)

numbers = []

print('-Теперь вводите числа')
for _ in range(nums):
    n = input('-')
    numbers.append(n)


def translate_number(number, system):
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    number = str(number)
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


print('-Теперь давайте выберем диапазон систем счисления. Каково нижние значение диапазона?')

start = input('-')
while not start.isdigit():
    print('-Давайте всё-так число')
    start = input('-')
start = int(start)
print('-А теперь верхние значение диапазона систем счисления')

end = input('-')
while not end.isdigit():
    print('-Давайте всё-так число')
    end = input('-')
end = int(end)

if start > end:
    start, end = end, start


for i in range(start, end+1):
    this_num = translate_number(sum_num, i)
    a = 0
    for j in range(len(numbers)):
        a += translate_number(numbers[j], i)
    if a == this_num:
        print("-Вот необходимая вам система счисления:", i)
        break
else:
    print('-Простите, но в данном диапазоне совпадений не найдено')