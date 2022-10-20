class HashTable(object):
    def __init__(self, length):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)

        return sum(ord(c) for c in str(key)) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for pos in self.array[index]:
                if pos[0] == key:
                    pos[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])



    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            return None
        for pos in self.array[index]:
            if pos[0] == key:
                return pos[1]

        return None

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
            if pos is not None:
                stringOut = stringOut + str(pos)[1:-1]
        return stringOut