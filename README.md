# Simulador de Autômatos Finitos

Este é um projeto para a matéria de Linguagens Formais e Autômatos com o intuito de criar um Simulador de Autômato Finito para validação de palavras (strings).
No mesmo programa é possível testar para 3 tipos de Autômatos Finitos:
  - Autômato Finito Determinístico (DFA).
  - Autômato Finito Não-Determinístico (NFA).
  - Autômato Finito Não-Determinístico com Transição Vazia (e-NFA).

## Requisitos
  - Python 3.10.5 ou superior (testado somente nessa versão, possivelmente funciona em versões de Python 3.x.x).
  - Windows 10 ou superior (testado somente nesse sistemas operacional, possivelmente funciona em outros, como Mac e Linux).
  
## Preparação das entradas
  Antes de executar é necessário colocar os arquivos de entrada em seus devidos lugares:
  
  1. Colocar dentro da pasta [*input*](input/) o(s) arquivos(s) de texto (.txt) com a(s) tabela(s) de transições dos autômatos.   
  
      A tabela deve seguir o seguinte modelo:
      - Na primeira linha terão os símbolos do alfabeto.
      - Na primeira coluna terão os estados.
      - Nas colunas seguintes terão as transições.
      - Os estados inicias devem ser marcados com ">".
      - Os estados finais devem ser marcados com "*".
      - As colunas devem ser separadas por espaço em branco.
      - No e-NFA o símbolo de vazio é representado por *&*.

        Exemplo da tabela de um DFA, assim como em [*ex_dfa.txt*](input/ex_dfa.txt):
        ```
              0	  1
        >*q0  q2  q1
        q1    q3  q0
        q2    q3  q3
        q3    q1  q2
        ```

        Exemplo da tabela de um NFA, assim como em [*ex_nfa.txt*](input/ex_nfa.txt):
        ```
              0         1
        >q0   {q0,q1}   {q0}
        q1    {q2,q3}   {q4}
        q2    {q0,q2}   {q4}
        *q3   {}        {}
        *q4   {}        {}
        ```

        Exemplo de tabela de um e-NFA, assim como em [*ex_e-nfa.txt*](input/ex_e-nfa.txt):
        ```
              a       b       &
        >q0   {}      {}      {q1}
        q1    {}      {}      {q2,q4}
        q2    {q3}    {}      {}
        q3    {}      {}      {q6}
        q4    {}      {q5}    {}
        q5    {}      {}      {q6}
        q6    {}      {}      {q1,q7}
        q7    {q8}    {}      {}
        q8    {}      {q9}    {}
        q9    {}      {q10}   {}
        *q10  {}      {}      {}
        ```
    
  2. Colocar dentro da mesma pasta [*input*](input/) o(s) arquivos(s) de texto (.txt) com a(s) palavra(s) a ser(em) testada(s)
    - Cada palavra deve estar em uma linha.
    
      Exemplo de palavras, assim como em [*ex_strings.txt*](input/ex_strings.txt):
      ```
      0
      101
      001
      10101010101
      010001001
      010101
      101010100101011111
      10101011
      101010000100101010
      1000011
      ```

## Como executar
  Para executar o programa é necessário seguir os passos a seguir:
  1. No seu terminal favorito, digite `python main.py` (em alguns casos é necessário especificar a versão do Python, como `python3 main.py`).
  2. Logo após será pedido para digitar o nome do arquivo onde está a tabela de transições, como por exemplo: `ex_dfa.txt` ou somente `ex_dfa`.
  3. Logo após será pedido para digitar o nome do arquivo onde estão as palavras a serem testadas, como por exemplo: `ex_strings.txt` ou somente `ex_strings`.
