import time
import random
import matplotlib.pyplot as plt
import shell_sort_array

def benchmark_array(sizes, scenario="medium"):
    times = []
    for n in sizes:
        if scenario == "best":
            arr = list(range(n))
        elif scenario == "worst":
            arr = list(range(n, 0, -1))
        else: # medium
            arr = list(range(n))
            random.shuffle(arr)
            
        start = time.perf_counter()
        shell_sort_array.shell_sort(arr)
        end = time.perf_counter()
        times.append(end - start)
        print(f"Array {scenario} N={n}: {end-start:.4f}s")
    return times

def main():
    sizes = [100, 500, 1000, 2000, 5000, 7500, 10000]

    print("Iniciando Benchmarks para Vetor (Array)...")
    medium_times = benchmark_array(sizes, "medium")
    best_times = benchmark_array(sizes, "best")
    worst_times = benchmark_array(sizes, "worst")

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes, medium_times, marker='o', linestyle='-', color='b', label='Caso Médio (Aleatório)')
    plt.plot(sizes, best_times, marker='s', linestyle='--', color='g', label='Melhor Caso (Ordenado)')
    plt.plot(sizes, worst_times, marker='^', linestyle=':', color='r', label='Pior Caso (Inverso)')

    plt.title('Shell Sort Performance: Vetor (Array)')
    plt.xlabel('Tamanho da Entrada (N)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    save_path = 'performance_graph.png'
    plt.savefig(save_path)
    print(f"\nGráfico atualizado salvo em: {save_path}")

if __name__ == "__main__":
    main()
