class SymbolClassifier:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.all =[]
        self.classify()

    def classify(self) -> None:
        with open('Tokens.in', 'r') as f:
            f.readline()
            for i in range(10):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
                self.all.append(separator)
            for i in range(15):
                item = f.readline().strip()
                self.operators.append(item)
                self.all.append(item)
            for i in range(21):
                item = f.readline().strip()
                self.reservedWords.append(item)
                self.all.append(item)