qwes = []

while qwes != 'нет':

    new_text = input("Введите текст:")
    _letter = input('Введите постоянную согласную букву(с, б, з, ф или к):')
    _letter_list = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я',
                    'А', 'О', 'И', 'Е', 'Ё', 'Э', 'Ы', 'У', 'Ю', 'Я']

    for z in _letter_list:
        _rep = z + _letter + z.lower()
        new_text = new_text.replace(z, _rep)

    print(new_text)

    qwes = input('Еще один перевод?(Ответьте да или нет:)')

