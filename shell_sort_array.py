import time
import random

def shell_sort(arr):
    """
    Ordena um array nativo usando o algoritmo Shell Sort.
    Complexidade de espaço: O(1).
    Complexidade de tempo: Depende da sequência de gaps (Shell: O(n^2)).
    """
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Realiza trocas enquanto o elemento na posição j-gap for maior que temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def run_performance_tests():
    N = 5000
    scenarios = [
        ("best", "Melhor Caso (Ordenado)"),
        ("medium", "Caso Médio (Aleatório)"),
        ("worst", "Pior Caso (Inverso)")
    ]
    
    print(f"--- Iniciando Testes de Shell Sort em Array Nativo (N={N}) ---")
    print("-" * 60)
    
    for key, name in scenarios:
        if key == "best":
            arr = list(range(N))
        elif key == "medium":
            arr = list(range(N))
            random.shuffle(arr)
        elif key == "worst":
            arr = list(range(N, 0, -1))
        
        # Medição precisa com perf_counter
        start_time = time.perf_counter()
        shell_sort(arr)
        end_time = time.perf_counter()
        
        duration = end_time - start_time
        print(f"{name:<25}: {duration:.6f} segundos")
    
    print("-" * 60)
    print("Testes concluídos.")

if __name__ == "__main__":
    run_performance_tests()
