class FiniteAutomata:

    def __init__(self, states: list, alphabet: list, initialState, finals: list, transitions: dict):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initialState = initialState
        self.finals = finals

    def isDFA(self):
        for elem in self.transitions.keys():
            if len(self.transitions[elem]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        print(sequence)
        if self.isDFA():
            current = self.initialState
            for symbol in sequence:
                if (current, symbol) in self.transitions.keys():
                    current = self.transitions[(current, symbol)][0]
                else:
                    return False
            return current in self.finals
        return False

    def __str__(self):
        return "States = { " + ', '.join(self.states) + " }\n" \
               "Alphabet = { " + ', '.join(self.alphabet) + " }\n" \
               "Initial State = { " + self.initialState + " }\n" \
               "Transitions = { " + str(self.transitions) + " } \n" \
               "Final states = { " + ', '.join(self.finals) + " }\n"
