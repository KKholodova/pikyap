# Пример:

# data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# Unique(data) будет последовательно возвращать только 1 и 2

# data = [‘a’, ‘A’, ‘b’, ‘B’, ‘a’, ‘A’, ‘b’, ‘B’]
# Unique(data) будет последовательно возвращать только a, A, b, B

class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self.seen = set()
        self.ignore_case = ignore_case
        self.items = items
        self.index = 0

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item
        raise StopIteration()

    def __iter__(self):
        return self

# пример использования
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_iterator1 = Unique(data1)
for item in unique_iterator1:
    print(item)

data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_iterator2 = Unique(data2, ignore_case=False)
for item in unique_iterator2:
    print(item)