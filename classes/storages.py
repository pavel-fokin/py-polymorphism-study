class Memory:
    def info(self):
        print(type(self).__name__)

    def add(self, item: dict):
        print(f"put {item} to the storage")

    def get(self, pk: int):
        print(f"get item with {pk=}")


class Persistent:
    def info(self):
        print(type(self).__name__)

    def add(self, item: dict):
        print(f"put {item} to the storage")

    def get(self, pk: int):
        print(f"get item with {pk=}")
