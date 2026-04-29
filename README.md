# Shell Sort Implementation

**Grupo 3 — Shell Sort (vetor)**

### Participantes:
- Leonardo Felipe Roncolato
- Ana Clara Nery e Mello Figueiredo
- Maria Clara Rossetti A L Manrique
- Paulo Rocha Lima de Souza
- Laryssa Fernanda Alves Santos
- Pedro Augusto Bandeira Viana
- Guilherme Emanuel Oliveira Guimarães

---

Este repositório contém diferentes implementações do algoritmo **Shell Sort** em Python, explorando o impacto de estruturas de dados na performance.

## Estruturas Implementadas

### 1. Array Nativo (`shell_sort_array.py`)
*   **Tamanho do teste ($N$):** 5000
*   **Performance:** Extremamente alta devido ao acesso aleatório $O(1)$.
*   **Uso:** Ideal para produção e grandes volumes de dados.

### 2. Lista Simplesmente Encadeada (`shell_sort_linked_list.py`)
*   **Tamanho do teste ($N$):** 1000
*   **Performance:** Baixa devido ao custo de travessia $O(n)$ para acessar cada gap.
*   **Uso:** Fins acadêmicos para demonstrar limitações de estruturas de dados.

### 3. Implementação Alternativa (`shell-sort-guilherme.py`)
*   Arquivo enviado pelo aluno Guilherme.

## Como Executar

Para rodar a versão com **Array**:
```bash
python3 shell_sort_array.py
```

Para rodar a versão com **Linked List**:
```bash
python3 shell_sort_linked_list.py
```

---

## Análise de Performance e Gráfico

Abaixo, o gráfico gerado automaticamente comparando as duas implementações:

![Performance Graph](performance_graph.png)

### Observações sobre os dados coletados:
- **Array Nativo:** Consegue processar $N=5000$ em menos de 0.01 segundos.
- **Linked List:** Leva quase 0.40 segundos para processar apenas $N=1000$.

## Análise de Complexidade Assintótica

### 1. Array (Caso Base)
No Shell Sort convencional sobre um array:
- **Espaço:** $O(1)$ (In-place).
- **Tempo:** Varia conforme a sequência de gaps. Para a sequência de Shell ($N/2^k$), o pior caso é $O(N^2)$. No entanto, como o acesso ao índice `arr[j]` é **$O(1)$**, o custo dominante são as comparações e trocas.

### 2. Lista Encadeada (Caso Crítico)
Nesta implementação, a estrutura de dados introduz um gargalo significativo:
- **Acesso ao Nó:** Para encontrar o nó no índice `j` ou `j-gap`, usamos o método `get_node_at(index)`, que percorre a lista desde a cabeça. Isso tem custo **$O(index)$**, que no caso médio é **$O(N)$**.
- **Custo Acumulado:**
    - O algoritmo possui três loops principais: Gaps ($\log N$), Iteração ($N$) e Inserção ($N/gap$).
    - Dentro do loop mais interno, chamamos `get_node_at` múltiplas vezes.
    - Isso eleva a complexidade total para aproximadamente **$O(N^3)$** no pior caso, ou **$O(N^2 \log N)$** se considerarmos a amortização dos gaps.

**Conclusão:** O Shell Sort é um algoritmo que "salta" elementos. Listas simplesmente encadeadas são inerentemente ruins para "saltos", pois só permitem navegação sequencial. Para ordenar listas encadeadas, algoritmos como **Merge Sort** são muito mais eficientes, pois trabalham com divisões sequenciais.

---
