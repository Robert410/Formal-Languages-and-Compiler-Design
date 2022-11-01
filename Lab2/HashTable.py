class HashTable(object):
    def __init__(self, length):
        self.array = [[] for _ in range(length)]

    def hash(self, key):
        length = len(self.array)

        return sum(ord(c) for c in str(key)) % length

    def contains(self, key) -> bool:
        return key in self.array[self.hash(key)]

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for pos in self.array[index]:
                if pos[0] == key:
                    # key already exists, update the value
                    pos[1] = value
                    break
            else:
                # key doesn't exist but index does (there previously was a value there)
                self.array[index].append([key, value])
        else:
            # key and index don't exist
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        list_position = self.hash(key)
        list_index = 0
        for item in self.array[list_position]:
            if item != key:
                list_index += 1
            else:
                break
        return (list_position, list_index)

    def delete(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            return None
        for pos in self.array[index]:
            if pos[0] == key:
                del self.array[index]

    def __str__(self):
        stringOut = ""
        for pos in self.array:
            if pos != None and pos != []:
                stringOut = stringOut + str(pos)[1:-1]
                stringOut += "\n"
        return stringOut