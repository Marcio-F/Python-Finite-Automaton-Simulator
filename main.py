from src.finite_automaton_simulator import *

def main():
    print('--------------Simulador de Autômatos Finitos--------------\n')
    
    automaton = None
    transitionsFile = str()
    while automaton == None:
        try:
            transitionsFile = str(input('Digite o nome do arquivo de texto da tabela de transições (dentro da pasta input) do DFA: '))
            
            if not transitionsFile.endswith('.txt'):
                transitionsFile += '.txt'
            
            automaton = readautomaton('./input/' + transitionsFile)
        except FileNotFoundError:
            print('Arquivo ' + transitionsFile + ' não encontrado!\n')
    
    words = None
    inputFile = str()
    while words == None:
        try:
            inputFile = str(input('Digite o nome do arquivo de texto de entrada com as strings (dentro da pasta input) a serem testadas: '))
            
            if not inputFile.endswith('.txt'):
                inputFile += '.txt'
            
            words = readWords('./input/' + inputFile)
        except FileNotFoundError:
            print('Arquivo ' + inputFile + ' não encontrado!\n')
    
    outputFile = './output/' + transitionsFile.replace('.txt', '_output.txt')
    writeResults(automaton, words, outputFile)
    
    print()

if __name__ == '__main__':
    main()