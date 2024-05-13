import ujson  # type: ignore # Biblioteca para manipulação de JSON em MicroPython

def update_count(count):
    data = {"count": count}
    with open('contador.json', 'w') as file:
        ujson.dump(data, file)

def get_count():
    try:
        with open('contador.json', 'r') as file:
            data = ujson.load(file)
            count = data.get('count', 0)
    except OSError:
        count = 0
    return count