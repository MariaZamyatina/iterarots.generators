import itertools


class FlatIterator:

    def __init__(self, list_of_list):
        list_temporary = []

        def get_list_append(list_of_list):
            for item in itertools.chain(*list_of_list):
                if isinstance(item, list):
                    get_list_append(item)
                else:
                    list_temporary.append(item)
            return list_temporary

        self.list_of_list = get_list_append(list_of_list)

    def __iter__(self):
        self.list = iter(self.list_of_list)
        return self

    def __next__(self):
        if self.list:
            return next(self.list)
        else:
            raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


