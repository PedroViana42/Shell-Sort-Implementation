import time
import random
import matplotlib.pyplot as plt
import shell_sort_array
from shell_sort_linked_list import LinkedList, generate_test_case

def benchmark_array(sizes):
    times = []
    for n in sizes:
        arr = list(range(n))
        random.shuffle(arr)
        start = time.perf_counter()
        shell_sort_array.shell_sort(arr)
        end = time.perf_counter()
        times.append(end - start)
        print(f"Array N={n}: {end-start:.4f}s")
    return times

def benchmark_linked_list(sizes):
    times = []
    for n in sizes:
        ll = generate_test_case("medium", n)
        start = time.perf_counter()
        ll.shell_sort()
        end = time.perf_counter()
        times.append(end - start)
        print(f"LinkedList N={n}: {end-start:.4f}s")
    return times

def main():
    # Definindo tamanhos de entrada (N)
    # LinkedList é muito lenta, então usamos valores menores
    sizes_array = [100, 500, 1000, 2000, 3000, 5000]
    sizes_ll = [100, 250, 500, 750, 1000]

    print("Iniciando Benchmarks...")
    array_times = benchmark_array(sizes_array)
    ll_times = benchmark_linked_list(sizes_ll)

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes_array, array_times, marker='o', linestyle='-', color='b', label='Array (Nativo)')
    plt.plot(sizes_ll, ll_times, marker='s', linestyle='--', color='r', label='Linked List (Custom)')

    plt.title('Shell Sort Performance: Array vs Linked List')
    plt.xlabel('Tamanho da Entrada (N)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    # Adicionando anotação sobre a disparidade
    plt.annotate('O(n²) no Array', xy=(sizes_array[-1], array_times[-1]), xytext=(sizes_array[-1]-1000, array_times[-1]+0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.annotate('O(n³) na LinkedList (devido ao acesso O(n))', xy=(sizes_ll[-1], ll_times[-1]), xytext=(sizes_ll[-1]-500, ll_times[-1]+0.5),
                 arrowprops=dict(facecolor='red', shrink=0.05))

    save_path = 'performance_graph.png'
    plt.savefig(save_path)
    print(f"\nGráfico salvo com sucesso em: {save_path}")

if __name__ == "__main__":
    main()
