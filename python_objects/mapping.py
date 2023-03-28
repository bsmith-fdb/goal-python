class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update  # private copy of the method implementation, gets renamed to _Mapping__update


class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

    def print_something(self):
        print("Print something")

    __print_something = print_something


if __name__ == "__main__":
    # print(Mapping.__update) # fails
    print(dir(Mapping))
