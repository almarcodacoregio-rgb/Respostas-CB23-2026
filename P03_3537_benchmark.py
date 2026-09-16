import AP_03_ordenacao as ap
import time
import random
import sys

sys.setrecursionlimit(10000)

random.seed(1001)

#Criar funções auxiliares para gerar listas aleatórias (caso médio) e listas invertidas/desfavoráveis (pior caso) para múltiplos valores de N (por exemplo, N = 100, 500, 1000, 5000).

def test_aleatorio(n, function, m):
    t = []
    for i in range(m):
        X = random.sample(range(1, n+1), n)

        inicio = time.perf_counter()
        function(X)
        fim = time.perf_counter()

        t.append(fim - inicio)
    sum_t = sum(t)/m

    return sum_t

def test_invertido(n, function, m):
    t = []
    for i in range(m):
        X = list(range(n, 0, -1))

        inicio = time.perf_counter()
        function(X)
        fim = time.perf_counter()

        t.append(fim - inicio)
    sum_t = sum(t)/m

    return sum_t


casos_n = (100, 500, 1000, 5000); m = 50
funcoes = (ap.selection_sort, ap.divide_and_conquer_sort, ap.quick_sort)

#Criar tabela  Exibir no terminal uma tabela organizada com os resultados de cada algoritmo, N, cenário e tempo médio.

def tabela_resultados():
    print(f"{'Algoritmo':<30} {'N':<10} {'Cenário':<20} {f'Tempo Médio(s)-{m}x':<20}")
    print("-" * 85)
    for f in funcoes:
        for n in casos_n:
            for scenario in ['caso médio', 'caso pior']:
                if scenario == 'caso médio':
                    t = test_aleatorio(n, f, m)
                else:
                    t = test_invertido(n, f, m)

                print(f"{f.__name__:<30} {n:<10} {scenario:<20} {t:<20.10f}")
            print("-" * 85)

tabela_resultados()
