### Домашняя работа по лекции «Итераторы, генераторы»

[задание](https://github.com/netology-code/py-homeworks-advanced/tree/master/2.Iterators.Generators.Yield)

------

- Для плоского представления списка вида : 
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]

    доработан класс FlatIterator в [itetator1.py]() и функция [flat_generator]()
    в [generator1.py]()
-  Для плоского представления списка вида 
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    доработан класс в [iterator2.py]() и функция в [generator2.py]()