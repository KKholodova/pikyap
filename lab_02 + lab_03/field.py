# Необходимо реализовать генератор field. Генератор field последовательно выдает значения ключей словаря

def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            key = args[0]
            if key in item and item[key] is not None:
                yield item[key]
        else:
            filtered_item = {key: item[key] for key in args if key in item and item[key] is not None}
            if filtered_item:
                yield filtered_item


# пример использования
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

# проверка для одного аргумента
for title in field(goods, 'title'):
    print(title)

# проверка для двух аргументов
for item in field(goods, 'title', 'price'):
    print(item)
