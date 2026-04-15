# Shell Sort em Linked List

Este projeto implementa o algoritmo Shell Sort utilizando uma estrutura de **Lista Simplesmente Encadeada** (Singly Linked List) em Python, comparando tempos de execução em três cenários diferentes.

## Como Executar

Para rodar o script e ver os tempos de execução:
```bash
python3 shell_sort_linked_list.py
```

## Explicação Técnica

O Shell Sort é uma extensão do Insertion Sort que permite a troca de elementos distantes entre si através de um "gap" (intervalo). Embora seja eficiente em arrays, sua performance degrada significativamente ao ser aplicado em listas encadeadas.

### O Problema do Acesso Aleatório

A principal razão para a ineficiência reside na natureza do acesso aos dados:

1.  **Arrays (O(1)):** O acesso a qualquer elemento pelo seu índice é imediato.
2.  **Listas Encadeadas (O(n)):** Para acessar um nó em um índice específico, é necessário percorrer a lista desde a cabeça (`head`).

### Impacto na Complexidade

No Shell Sort, para cada elemento no loop externo, realizamos múltiplas buscas de nós em posições distantes:
-   No melhor caso (array), a complexidade é aproximadamente $O(n \log n)$.
-   Na lista encadeada, como cada "acesso indexado" custa $O(n)$, a complexidade real acaba sendo multiplicada, resultando em algo próximo de **$O(n^2 \log n)$** ou pior.

### Conclusão

Embora a lógica de gaps ainda funcione, o **custo de travessia** anula os benefícios de "pular" elementos. Em listas encadeadas, algoritmos como Merge Sort são muito mais adequados por tirarem proveito da estrutura sequencial.
