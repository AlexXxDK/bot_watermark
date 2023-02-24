from json import loads
from pathlib import Path
from datetime import datetime


def parse_config(name: str) -> dict:
    try:
        with open(f'data/{name}.json', 'r') as file:
            return loads(file.read())
    except FileNotFoundError:
        print(f'Конфиг файла с именем {name} не существует!')


def now_datetime() -> datetime:
    return datetime.now()


def get_parent_root() -> Path:
    return Path(__file__).parent.parent
