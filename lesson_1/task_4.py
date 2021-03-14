"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# Сложность этого алгоритма O(n)
def login(data):
    for key in data.keys():
        if 'YES' in data[key]['activation_mark']:
            print('Учетка  Активирована')
        elif 'NO' in data[key]['activation_mark']:
            print('Учетка Не Активирована')


rep = {
    'user1': {'login': 'john1995',
              'password': 'kati198',
              'activation_mark': 'YES',
              },

    'user2': {'login': 'paul988',
              'password': 'kta125',
              'activation_mark': 'NO',
              },
    'user3': {'login': 'simeon789',
              'password': 'kala693',
              'activation_mark': 'NO',
              },
    'user4': {'login': 'simon789',
              'password': 'kaja693',
              'activation_mark': 'YES',
              },
}
print(login(rep))

print()


# Сложность этого алгоритма O(1)
class Login:
    def __init__(self, login, password, activation_mark):
        self.login = login
        self.password = password
        self.activation_mark = activation_mark

    def show(self):
        if self.activation_mark == 'YES':
            print('Учетка  Активирована')
        elif self.activation_mark == 'NO':
            print('Учетка  Не Активирована')


c = Login(login='kj12', password='v8f', activation_mark='YES')
c.show()
c = Login(login='rj2', password='8yuf', activation_mark='NO')
c.show()
