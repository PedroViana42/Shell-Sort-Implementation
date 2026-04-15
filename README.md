# Shell Sort Implementation

Este repositório contém duas implementações do algoritmo **Shell Sort** em Python, explorando o impacto de diferentes estruturas de dados na performance do algoritmo.

## Estruturas Implementadas

### 1. Array Nativo (`shell_sort_array.py`)
*   **Tamanho do teste ($N$):** 5000
*   **Performance:** Extremamente alta devido ao acesso aleatório $O(1)$.
*   **Uso:** Ideal para produção e grandes volumes de dados.

### 2. Lista Simplesmente Encadeada (`shell_sort_linked_list.py`)
*   **Tamanho do teste ($N$):** 1000
*   **Performance:** Baixa devido ao custo de travessia $O(n)$ para acessar cada gap.
*   **Uso:** Fins acadêmicos para demonstrar limitações de estruturas de dados.

## Como Executar

Para rodar a versão com **Array**:
```bash
python3 shell_sort_array.py
```

Para rodar a versão com **Linked List**:
```bash
python3 shell_sort_linked_list.py
```

## Explicação Técnica

O Shell Sort é uma extensão do Insertion Sort que permite a troca de elementos distantes entre si através de um "gap" (intervalo). A eficiência deste "salto" depende diretamente da velocidade de acesso aos elementos.

### O Problema do Acesso Aleatório

1.  **Arrays (O(1)):** O acesso a qualquer elemento pelo seu índice é imediato. O Shell Sort tira proveito pródigo desta propriedade.
2.  **Listas Encadeadas (O(n)):** Para acessar um nó em um índice específico (necessário para calcular o gap), a estrutura percorre todos os nós anteriores. Isso torna o algoritmo substancialmente mais lento.

### Comparação de Performance

| Estrutura | $N$ | Tempo Médio (aprox.) |
| :--- | :--- | :--- |
| Array | 5000 | ~0.05 segundos |
| Linked List | 1000 | ~1.80 segundos |

> [!IMPORTANT]
> Note que mesmo com um $N$ cinco vezes maior, a versão com array é ordens de magnitude mais rápida que a versão com lista encadeada.
