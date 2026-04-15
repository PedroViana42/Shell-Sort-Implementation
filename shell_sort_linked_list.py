import time
import random

class Node:
    """Representa um nó em uma lista simplesmente encadeada."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Implementação básica de uma lista simplesmente encadeada com Shell Sort."""
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """Adiciona um novo valor ao final da lista."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get_node_at(self, index):
        """Retorna o nó em um índice específico. Custo: O(n)."""
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def shell_sort(self):
        """
        Ordena a lista usando o algoritmo Shell Sort.
        Realiza trocas de valores entre os nós.
        A lógica de gaps segue N/2, N/4, ..., 1.
        """
        n = self.size
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                # Armazena o valor do nó atual (i) para inserção
                node_i = self.get_node_at(i)
                temp_val = node_i.value
                
                j = i
                # Realiza a ordenação por inserção para o gap atual
                while j >= gap:
                    node_prev = self.get_node_at(j - gap)
                    if node_prev.value > temp_val:
                        # Move o valor do nó (j-gap) para o nó (j)
                        node_j = self.get_node_at(j)
                        node_j.value = node_prev.value
                        j -= gap
                    else:
                        break
                
                # Coloca o valor temporário no seu local correto
                node_fill = self.get_node_at(j)
                node_fill.value = temp_val
                
            gap //= 2

def generate_test_case(scenario, n):
    """Gera uma LinkedList com base no cenário solicitado."""
    ll = LinkedList()
    if scenario == "best":
        # Melhor caso: Já ordenado
        arr = list(range(n))
    elif scenario == "medium":
        # Caso médio: Aleatório
        arr = list(range(n))
        random.shuffle(arr)
    elif scenario == "worst":
        # Pior caso: Ordem decrescente
        arr = list(range(n, 0, -1))
    
    for val in arr:
        ll.append(val)
    return ll

def run_performance_tests():
    N = 1000
    scenarios = [
        ("best", "Melhor Caso (Ordenado)"),
        ("medium", "Caso Médio (Aleatório)"),
        ("worst", "Pior Caso (Inverso)")
    ]
    
    print(f"--- Iniciando Testes de Shell Sort em Lista Encadeada (N={N}) ---")
    print("-" * 60)
    
    for key, name in scenarios:
        ll = generate_test_case(key, N)
        
        # Medição precisa do tempo
        start_time = time.perf_counter()
        ll.shell_sort()
        end_time = time.perf_counter()
        
        duration = end_time - start_time
        print(f"{name:<25}: {duration:.6f} segundos")
    
    print("-" * 60)
    print("Testes concluídos.")

if __name__ == "__main__":
    run_performance_tests()
