import random
 
def shell_sort(vetor):
    n = len(vetor)
    # 1. Definir a sequência de gaps (n/2, n/4, ..., 1)
    gap = n // 2 
 
    print(f"VETOR ORIGINAL: {vetor}")
    print("-" * 60)
 
    # O processo continua enquanto o gap for maior que zero
    while gap > 0:
        print(f"Executando com GAP = {gap}:")
        
        # Realiza a ordenação por inserção para os elementos no gap atual
        for i in range(gap, n):
            temp = vetor[i]
            j = i
            
            # Comparação e deslocamento dos elementos
            while j >= gap and vetor[j - gap] > temp:
                vetor[j] = vetor[j - gap]
                j -= gap
            
            vetor[j] = temp
        
        # REQUISITO: Exibir o estado do vetor a cada mudança de GAP
        print(f"Estado atual:  {vetor}")
        print("-" * 40)
        
        gap //= 2  # Redução do gap (ex: 5 -> 2 -> 1)
 
    print(f"VETOR FINAL ORDENADO: {vetor}")
 
# --- Demonstração com os 3 Casos de Teste (10 elementos cada) ---
 
def executar_trabalho():
    # CASO 1: ALEATÓRIO
    print("\n" + "="*20 + " TESTE 1: CASO ALEATÓRIO " + "="*20)
    dados_aleatorios = random.sample(range(1, 100), 10)
    shell_sort(dados_aleatorios)
 
    # CASO 2: QUASE ORDENADO (Apenas 2 ou 3 fora de ordem)
    print("\n" + "="*20 + " TESTE 2: CASO QUASE ORDENADO " + "="*18)
    dados_quase = [10, 20, 40, 30, 50, 60, 80, 70, 90, 100]
    shell_sort(dados_quase)
 
    # CASO 3: INVERSO (Do maior para o menor)
    print("\n" + "="*20 + " TESTE 3: CASO INVERSO " + "="*22)
    dados_inverso = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]
    shell_sort(dados_inverso)
 
if __name__ == "__main__":
    executar_trabalho()
 