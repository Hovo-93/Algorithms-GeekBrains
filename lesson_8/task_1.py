import collections
import operator


class Leaf:
    """ Вспомогательный класс Лист для создания дерева Хаффмана
        char -символ из кодируемой строки
        value -частота буквы в строке
    """

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf:char "{self.char}" value{self.value}'


class Node:
    """Воспомогательный класс Узел для построения алгоритма Хаффмана"""

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node: value{self.value} \nleft->{self.left} \nright->{self.right}'

class Haffman:
    """Основной класс для реализации алго   ритма Хаффмана"""

    def __init__(self):
        self._code_table = {}

    def _get_table(self, tree, code=''):
        """Рекурсивный обход дерева и построение таблицы крдирования"""
        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self._code_table[tree.char] = code

    def encode(self, string, detail=False):
        """Метод для кодирования строки"""
        self._code_table = {}
        count = collections.Counter(string)
        array = collections.deque(map(Leaf, count.most_common()))
        if detail:
            print(array)  # Массив из листьев

        while len(array) > 1:  # Формируем дерево
            array = collections.deque(sorted(array, key=operator.attrgetter('value')))
            leaf_small = array.popleft()
            leaf_bigger = array.popleft()
            array.append(Node(leaf_small.value + leaf_bigger.value, leaf_small, leaf_bigger))
        tree = array.pop()
        if detail:
            print(tree)  # Дерево Хаффмана
        self._get_table(tree)
        if detail:
            print(self._code_table)  # Таблица кодирования
        return ' '.join([self._code_table[char] for char in string])


if __name__ == '__main__':
    haf = Haffman()
    print(haf.encode('beep boop beer!'))

    print('*' * 50)
    my_str = input('Введите строку для кодирования ')
    print(haf.encode(my_str, detail=True))
