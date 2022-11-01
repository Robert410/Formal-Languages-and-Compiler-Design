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
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.PIF.add(tokens[i], "(" + str(line_counter) + ", " + str(position) + ")")

                    elif self.scanner.is_identifier(tokens[i]):
                        if ((i + 4) < len(tokens) is not None) :
                            if self.scanner.is_constant(tokens[i+4]):
                                self.ST.addSymTable(tokens[i], str(tokens[i+4]))
                            elif self.scanner.is_identifier(tokens[i+4]):
                                continue
                            else:
                                self.ST.addSymTable(tokens[i], "undefined")

                        self.PIF.add(tokens[i], "(" + str(line_counter) + ", " + str(position) + ")")
                    elif self.scanner.is_constant(tokens[i]):
                        self.ST.addSymTable(extra + tokens[i], " -> const variable")
                        self.PIF.add(tokens[i], "(" + str(line_counter) + ", " + str(position) + ")")
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            line_counter) + " column: " + str(position) + "\n"
                    position += len(tokens[i])
                    if i+1 < len(tokens):
                        if tokens[i+1] != " ":
                            exceptionMessage += 'Lexical error at line ' + str(
                                line_counter) + " column: " + str(position) + " (No spacing between elements)\n"


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