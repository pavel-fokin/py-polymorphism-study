class Storage:
    def info(self):
        print(type(self).__name__)

    def add(self, item: dict):
        raise NotImplementedError

    def get(self, pk: int):
        raise NotImplementedError


class Memory(Storage):
    def add(self, item: dict):
        print(f"put {item} to the storage")

    def get(self, pk: int):
        print(f"get item with {pk=}")


class Persistent(Storage):
    def add(self, item: dict):
        print(f"put {item} to the storage")

    def get(self, pk: int):
        print(f"get item with {pk=}")
