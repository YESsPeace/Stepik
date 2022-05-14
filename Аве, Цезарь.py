#Алфавит
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
english = eng_upper_alphabet + eng_lower_alphabet
#Алфавит

#Функция шифрования

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

#Функции шифрования


s = input().split() #Превращение строки в лист
output_s = []

for i in s:

    prog_i = ''
    for k in i: #Избавляет от знаков
        if k in english:
            prog_i += k

    key = len(prog_i) #Находим длину слова без знаков

    a = chef_eng(i, key)

    output_s.append(a)

print(*output_s, sep=" ")