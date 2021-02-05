from typing import List

source1 = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

source2 = [
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
]


# 11:26 Start time(Local Ufa)

def tree_builder(summits: List[tuple]):
    """
    Построитель деревьев
    :param summits: Перечень вершин дерева
    :return: Готовое дерево
    """
    tree = dict()
    num = 1
    added = list()

    def add_element(subtree: dict, new_element: tuple):
        for key, tr in subtree.items():
            # Если нашли родителя, то добавляем его, иначе углубляемсся в поддерево
            if key == new_element[0]:
                tr[new_element[1]] = dict()
                break
            else:
                add_element(tr, new_element)

    # Будем строить дерево до тех пор пока вершины добавляются
    while num is not None:
        num = None
        for n, summit in enumerate(summits):
            if num is None:
                # Проверка на дублирование вершин
                if summit[1] in added:
                    raise Exception('Wrong input data')

                # Добавляем корневые вершины
                if summit[0] is None:
                    tree[summit[1]] = dict()
                    added.append(summit[1])
                    num = n
                    break
                # Если знаем что элемент имеет родителя, то добавляем его
                if summit[0] in added:
                    add_element(tree, summit)
                    added.append(summit[1])
                    num = n
                    break

        # Удаляем из списка добавленный элемент
        if num is not None:
            summits.pop(num)
    return tree

print(tree_builder(source1))
print(tree_builder(source2))
# 12:15 End time(Local Ufa)

