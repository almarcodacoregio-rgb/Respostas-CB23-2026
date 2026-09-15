class _No:
    def __init__(self, valor=None, proximo=None):
        self.valor = valor
        self.proximo = proximo

class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self.contador = 0

    def push(self, item):
        """
        Insere um item no topo da pilha.

        Args:
            item: O elemento a ser inserido na pilha.

        Complexidade:
            O(1).
        """
        item_no = _No(item, self._topo)
        self._topo = item_no
        self.contador += 1

    def __len__(self):
        """
        Retorna a quantidade de elementos da pilha.

        Returns:
           o número de elementos da pilha.

        Complexidade:
            O(1).
        """
        return self.contador

    def esta_vazia(self):
        """
        Verifica se a pilha não contém elementos.

        Returns:
            bool: True se a pilha estiver vazia, False caso contrário.

        Complexidade:
            O(1).
        """
        if len(self) == 0: return True
        else: return False

    def pop(self):
        """
        Remove e retorna o item do topo.

        Returns:
            O item desempilhado do topo da pilha.

        Raises:
            IndexError: Se a pilha estiver vazia.

        Complexidade:
            O(1).
        """
        if self.esta_vazia() == True: raise IndexError("Pilha vazia")
        topo = self._topo.valor
        self._topo = self._topo.proximo
        self.contador -= 1
        return topo

    def topo(self):
        """
        Retorna o item do topo sem removê-lo.

        Returns:
            O valor do elemento que está atualmente no topo.

        Raises:
            IndexError: Se a pilha estiver vazia.

        Complexidade:
            O(1).
        """
        if self.esta_vazia() == True: raise IndexError("Pilha vazia")
        return self._topo.valor

    def __repr__(self):
        """
        Representação textual legível, do topo para a base.

        Returns:
            uma string contendo todos os valores da pilha.

        Complexidade:
            O(n).
        """
        if self.esta_vazia(): return ""
        topo = self._topo; lista_valores = []
        for _ in range(len(self)):
            lista_valores.append(str(topo.valor))
            topo = topo.proximo
        
        return " -> ".join(lista_valores)

