import abstract
import classes
import modules


def use_storage(storage):
    """Business case of storage usage."""

    storage.info()
    storage.add({"pk": 1, "data": "text"})
    storage.get(1)


if __name__ == "__main__":
    for storage in (
        # Abstract Class Case
        abstract.storages.Memory(),
        abstract.storages.Persistent(),

        # Duck Typed Case
        classes.storages.Memory(),
        classes.storages.Persistent(),

        # Modules Case
        modules.storages.memory,
        modules.storages.persistent,
    ):
        use_storage(storage)
        print()
