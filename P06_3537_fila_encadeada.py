import P06_3537_pilha_encadeada as p

class FilaEncadeada:
    def __init__(self):
        self.pilha_entrada = p.PilhaEncadeada()
        self.pilha_saida = p.PilhaEncadeada()

    def enfileirar(self, item):
        """
        Insere um elemento no fim da fila.

        Args:
            item: O elemento a ser inserido na fila.

        Complexidade:
            O(1).
        """
        self.pilha_entrada.push(item)

    def _transferir_se_necessario(self):
        """
        Transfere os elementos da pilha de entrada para a de saída se a saída estiver vazia.

        Raises:
            IndexError: Se a fila estiver vazia.

        Complexidade:
            O(n) no pior caso.
        """
        if self.pilha_saida.esta_vazia() == True:
            if self.pilha_entrada.esta_vazia() == True: raise IndexError("Fila vazia")
            self._transferir(self.pilha_entrada, self.pilha_saida)

    def desenfileirar(self):
        """
        Remove e retorna o elemento da frente da fila.

        Returns:
            O item removido da frente da fila.

        Raises:
            IndexError: Se a fila estiver vazia.

        Complexidade:
            O(1) amortizada. O(n) no pior caso.
        """
        self._transferir_se_necessario()
        return self.pilha_saida.pop()

    def frente(self):
        """
        Retorna o item da frente da fila sem removê-lo.

        Returns:
            O item localizado na frente da fila.

        Raises:
            IndexError: Se a fila estiver vazia.   

        Complexidade:
            O(1) amortizada. O(n) no pior caso.
        """
        self._transferir_se_necessario()
        return self.pilha_saida.topo()

    def __len__(self):
        """
        Retorna a quantidade total de elementos armazenados na fila.

        Returns:
            int: O número de elementos presentes na fila.

        Complexidade:
            O(1).
        """
        return len(self.pilha_entrada) + len(self.pilha_saida)

    def esta_vazia(self):
        """
        Verifica se a fila não contém elementos.

        Returns:
            bool: True se a fila estiver vazia, False caso contrário.

        Complexidade:
            O(1).
        """
        if len(self) == 0: return True
        else: return False

    def __repr__(self):
        """
        Retorna uma representação textual legível da fila, da frente para o fim.

        Returns:
            str: Elementos da fila unidos pelo separador ' <- '.

        Complexidade:
            O(n).
        """

        def _ler_valores(pilha):
                
                if pilha.esta_vazia() == True: return []
                lista_valores = []; pilha_temporaria = p.PilhaEncadeada()
                for _ in range(len(pilha)): 
                    topo_entrada = pilha.pop()
                    pilha_temporaria.push(topo_entrada)
        
                    lista_valores.append(str(topo_entrada))
        
                self._transferir(pilha_temporaria, pilha)
                return lista_valores

        if self.esta_vazia(): return ""
        lista_valores = _ler_valores(self.pilha_saida) + _ler_valores(self.pilha_entrada)[::-1]

        return " <- ".join(lista_valores)

    @staticmethod
    def _transferir(pilha1, pilha2):
        """
        Transfere todos os elementos da pilha1 para a pilha2.

        Args:
            pilha1: Pilha de origem dos elementos.
            pilha2: Pilha de destino dos elementos.

        Complexidade:
            O(n).
        """
        for _ in range(len(pilha1)): 
            topo_entrada = pilha1.pop()
            pilha2.push(topo_entrada)

