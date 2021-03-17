"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def chr_row(ascii_val=32):
    if ascii_val == 128:
        return True

    print(f'{ascii_val} -  {chr(ascii_val)}', end=' ')
    if (ascii_val) % 10 == 0:
        print('\n')
    chr_row(ascii_val + 1)


chr_row()
