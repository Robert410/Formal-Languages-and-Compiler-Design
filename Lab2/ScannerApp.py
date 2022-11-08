from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from ST import SymbolTable
from re import *

class ScannerResult:

    def __init__(self):
        self.ST = SymbolTable(20)
        self.PIF = ProgramInternalForm()
        self.scanner = Scanner()

    def compute_results(self, file_name: str):
        exceptionMessage = ""
        reserved_words = self.scanner.get_reserved_words()
        separators = self.scanner.get_separators()
        operators = self.scanner.get_operators()
        all = self.scanner.getAll()

        counterST = 0
        with open(file_name, 'r') as file:
            line_counter = 0
            for line in file:
                position = 0
                line_counter += 1
                tokens = self.scanner.get_tokens(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.PIF.add(tokens[i], all.index(tokens[i]) + 2)

                    elif self.scanner.is_identifier(tokens[i]):
                        id = self.ST.addSymTable(tokens[i])
                        counterST += 1
                        aux = list(id)
                        aux[0] = counterST
                        id = tuple(aux)
                        # print("id", id)
                        self.PIF.add(tokens[i], id)

                    elif self.scanner.is_constant(tokens[i]):
                        print(tokens[i])
                        const = self.ST.addSymTable(extra + tokens[i])
                        print(const)
                        counterST += 1
                        extra = ''
                        aux = list(const)
                        aux[0] = counterST
                        const = tuple(aux)
                        # print("const", const)
                        self.PIF.add(tokens[i], const)
                        # print(tokens[i] + " -> " + str(const))
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            line_counter) + " column: " + str(position) + "\n"
                    position += len(tokens[i])


        with open('st.out', 'w') as writer:
            writer.write(str(self.ST))
        with open('pif.out', 'w') as writer:
            writer.write(str(self.PIF))
        if exceptionMessage == '':
            print("Lexically correct")
        else:
            print(exceptionMessage)

if __name__ == '__main__':
    scanner_result = ScannerResult()
    # scanner_result.compute_results("p1.txt")
    # scanner_result.compute_results("p1err.txt")
    # scanner_result.compute_results("p2.txt")
    scanner_result.compute_results("p3.txt")

    # scanner = Scanner()
    # line = "println('hello world');"
    # print(line)
    # tokens = scanner.get_tokens(line)
    # print(tokens)