from finiteAutomata import FiniteAutomata


def processLine(line: str):
    return line.strip().split(' ')[2:]

class Utils:

    def readFromFile(file_name: str):
        with open(file_name) as file:
            states = processLine(file.readline())
            alphabet = processLine(file.readline())
            initialState = processLine(file.readline())[0]
            finals = processLine(file.readline())

            file.readline()

            transactions = {}
            for line in file:
                split = line.strip().split('=>')
                source = split[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = split[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = split[1].strip()

                if (source, route) in transactions.keys():
                    transactions[(source,route)].append(destination)
                else:
                    transactions[(source, route)] = [destination]

            return FiniteAutomata(states, alphabet, initialState, finals, transactions)