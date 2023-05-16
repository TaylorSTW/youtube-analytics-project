import json
from googleapiclient.discovery import build

API_KEY = "AIzaSyCJz5g7Zq8Q4KHyXe8wcWWAnE8wLz5aHpc"

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=API_KEY)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    def print_info(self) -> None:
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)
