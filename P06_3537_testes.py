import unittest

from P06_3537_pilha_encadeada import PilhaEncadeada
from P06_3537_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):

    def test_inicializacao(self):
        """Testa se a pilha nasce vazia e com tamanho 0"""
        pilha = PilhaEncadeada()
        self.assertTrue(pilha.esta_vazia())
        self.assertEqual(len(pilha), 0)

    def test_ordem_lifo(self):
        """Testa o comportamento Last-In, First-Out (Último a entrar, primeiro a sair)"""
        pilha = PilhaEncadeada()
        pilha.push(10)
        pilha.push(20)
        pilha.push(30)
        
        self.assertEqual(len(pilha), 3)
        self.assertEqual(pilha.topo(), 30)
        
        # O último a entrar (30) deve ser o primeiro a sair
        self.assertEqual(pilha.pop(), 30)
        self.assertEqual(pilha.pop(), 20)
        self.assertEqual(pilha.pop(), 10)
        self.assertTrue(pilha.esta_vazia())

    def test_excecao_pilha_vazia(self):
        """Testa se levanta IndexError ao manipular pilha vazia"""
        pilha = PilhaEncadeada()
        
        # O 'with self.assertRaises' verifica se o erro esperado realmente acontece
        with self.assertRaises(IndexError):
            pilha.pop()
            
        with self.assertRaises(IndexError):
            pilha.topo()

    def test_representacao_texto(self):
        """Testa o __repr__ da Pilha (do topo para a base)"""
        pilha = PilhaEncadeada()
        pilha.push("A")
        pilha.push("B")
        self.assertEqual(repr(pilha), "B -> A")


class TestFilaEncadeada(unittest.TestCase):

    def test_inicializacao(self):
        """Testa se a fila nasce vazia e com tamanho 0"""
        fila = FilaEncadeada()
        self.assertTrue(fila.esta_vazia())
        self.assertEqual(len(fila), 0)

    def test_ordem_fifo(self):
        """Testa o comportamento First-In, First-Out (Primeiro a entrar, primeiro a sair)"""
        fila = FilaEncadeada()
        fila.enfileirar("A")
        fila.enfileirar("B")
        fila.enfileirar("C")
        
        self.assertEqual(len(fila), 3)
        self.assertEqual(fila.frente(), "A")
        
        # O primeiro a entrar ("A") deve ser o primeiro a sair
        self.assertEqual(fila.desenfileirar(), "A")
        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(fila.desenfileirar(), "C")
        self.assertTrue(fila.esta_vazia())

    def test_alternancia_operacoes(self):
        """Testa enfileirar e desenfileirar de forma intercalada (testa a lógica das duas pilhas)"""
        fila = FilaEncadeada()
        fila.enfileirar(1)
        fila.enfileirar(2)
        
        self.assertEqual(fila.desenfileirar(), 1) # Fila: 2
        
        fila.enfileirar(3) # Fila: 2, 3
        
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)
        self.assertTrue(fila.esta_vazia())

    def test_excecao_fila_vazia(self):
        """Testa se levanta IndexError ao manipular fila vazia"""
        fila = FilaEncadeada()
        
        with self.assertRaises(IndexError):
            fila.desenfileirar()
            
        with self.assertRaises(IndexError):
            fila.frente()

    def test_representacao_texto(self):
        """Testa o __repr__ da Fila (da frente para o fim)"""
        fila = FilaEncadeada()
        fila.enfileirar(10)
        fila.enfileirar(20)
        self.assertEqual(repr(fila), "10 <- 20")

if __name__ == '__main__':
    unittest.main(verbosity=2)