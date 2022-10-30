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

        with open(file_name, 'r') as file:
            line_counter = 0
            for line in file:
                position = 0
                line_counter += 1
                tokens = self.scanner.get_tokens(line.strip())
                # print(tokens)
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.PIF.add(tokens[i], position)

                    elif self.scanner.is_identifier(tokens[i]):
                        id = self.ST.addSimTable(tokens[i])
                        # print("id", id)
                        self.PIF.add("id", id)
                    elif self.scanner.is_constant(tokens[i]):
                        const = self.ST.addSimTable(extra + tokens[i])
                        extra = ''
                        # print("const", const)
                        self.PIF.add("const", const)
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
    scanner_result.compute_results("p1err.txt")
    # scanner_result.compute_results("p2.txt")
    # scanner_result.compute_results("p3.txt")

    # scanner = Scanner()
    # line = "println('hello world');"
    # print(line)
    # tokens = scanner.get_tokens(line)
    # print(tokens)