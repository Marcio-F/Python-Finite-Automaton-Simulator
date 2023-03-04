class automaton:
    def __init__(self, states, alphabet, transitions, initial, final):
        self.states      = states
        self.alphabet    = alphabet
        self.transitions = transitions
        self.initial     = initial
        self.final       = final

    def getStates(self):
        return self.states

    def getAlphabet(self):
        return self.alphabet

    def getTransitions(self):
        return self.transitions

    def getInitial(self):
        return self.initial

    def getFinal(self):
        return self.final

    def setStates(self, states):
        self.states = states

    def setAlphabet(self, alphabet):
        self.alphabet = alphabet

    def setTransitions(self, transitions):
        self.transitions = transitions

    def setInitial(self, initial):
        self.initial = initial

    def setFinal(self, final):
        self.final = final

    def getTransition(self, state, symbol):
        if (state, symbol) in self.transitions:
            return self.transitions[(state, symbol)]
        else:
            return set()

    def isFinal(self, state):
        return state in self.final

    def isInitial(self, state):
        return state == self.initial

    def isState(self, state):
        return state in self.states

    def isSymbol(self, symbol):
        return symbol in self.alphabet

    def isTransition(self, state, symbol):
        return self.isState(state) and self.isSymbol(symbol) and bool(self.getTransition(state, symbol))

    def isFA(self):
        return all(self.isTransition(state, symbol) or self.getTransition(state, symbol) == set() 
                    for state in self.states for symbol in self.alphabet)

    def isAccepted(self, word):
        if not self.isFA():
            return False
        
        current_states = set([self.initial])
        for symbol in word:
            next_states = set()
            while next_states == set() and current_states != set():
                aux = set()
                epsilon_states = set()
                for state in current_states:
                    next_states |= self.getTransition(state, symbol)
                    epsilon_states |= self.getTransition(state, '&')
                aux |= next_states
                current_states = aux
                current_states |= epsilon_states

        return any(self.isFinal(state) for state in current_states)

    def __str__(self):
        states      = 'States: '        + str(self.states)
        alphabet    = '\nAlphabet: '    + str(self.alphabet)
        transitions = '\nTransitions: ' + str(self.transitions)
        initial     = '\nInitial: '     + str(self.initial)
        final       = '\nFinal: '       + str(self.final) + '\n'
        
        return states + alphabet + transitions + initial + final

def readAutomaton(filename):
    states      = list(str())
    alphabet    = list(str())
    transitions = dict()
    initial     = str()
    final       = list(str())

    with open(filename, 'r') as file:
        for line in file:
            if line[0].isspace():
                alphabet = line.strip().split()
                continue
            
            line = line.strip()
            if line.startswith('>'):
                line = line.replace('>', '')
                initial = line.split()[0].replace('*', '')
            if line.startswith('*'):
                line = line.replace('*', '')
                final += [line.split()[0]]
                
            states += [line.split()[0]]
            currentTranstions = line.split()[1:]
            for symbol, state in zip(alphabet, currentTranstions):
                if state != '{}':
                    transitions[(line.split()[0], symbol)] = {transition for transition in state.replace('{', '').replace('}', '').split(',')}

    return automaton(states, alphabet, transitions, initial, final)

def readWords(filename):
    words = list(str())
    
    with open(filename, 'r') as file:
        for line in file:
            words += [line.strip()]
    
    return words

def writeResults(automaton, words, outputFilename):
    accepted     = list(str())
    not_accepted = list(str())
    
    with open(outputFilename, 'w', encoding='utf-8') as file:
        for word in words:
            result = automaton.isAccepted(word) and 'Aceito    ' or 'Rejeitado '
            file.write(result + word + '\n')
            if result == 'Aceito    ':
                accepted += [word]
            else:
                not_accepted += [word]
    
    print('\n--------------Resultados--------------')
    print('\nArquivo de saída: ' + outputFilename)
    if accepted == []:
        print('\nNenhuma string aceita!')
    else:
        print(f'\nStrings aceitas ({len(accepted)}):')
        for word in accepted:
            print('  ' + word)
    
    if not_accepted == []:
        print('\nNenhuma string rejeitada!')
    else:
        print(f'\nStrings rejeitadas ({len(not_accepted)}):')
        for word in not_accepted:
            print('  ' + word)