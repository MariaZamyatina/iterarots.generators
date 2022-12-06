
class FlatIterator:
    def __init__(self, list_input):
        self.list_input = list_input

    def __iter__(self):
        self.list = iter([])
        self.list_input = iter(self.list_input)
        return self

    def __next__(self):
        try:
            item = next(self.list)
        except StopIteration:
            if not self.list_input:
                raise StopIteration
            self.list = iter(next(self.list_input))
            item = next(self.list)
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
