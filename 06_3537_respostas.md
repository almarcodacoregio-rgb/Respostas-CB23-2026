\*\*Matrícula:\*\* 3537  

\# Análise de Complexidade: Fila Encadeada com Duas Pilhas

\#\# Complexidade da Operação \`desenfileirar()\`

\#\#\# 1\. Pior Caso vs. Custo Amortizado

A operação \`desenfileirar()\` possui complexidade temporal de \*\*pior caso $O(N)$\*\* e \*\*complexidade amortizada $O(1)$\*\*.

\* \*\*Pior Caso ($O(N)$):\*\* Ocorre quando a \`pilha\_saida\` está vazia e a \`pilha\_entrada\` possui $N$ elementos. Para atender à remoção, a função \`\_transferir\_se\_necessario()\` precisa desempilhar todos os $N$ elementos da \`pilha\_entrada\` e empilhá-los na \`pilha\_saida\`. Esse processo executa $2N$ operações ($N$ chamadas de \`pop\` e $N$ chamadas de \`push\`), resultando em tempo linear $O(N)$.  
\* \*\*Custo Amortizado ($O(1)$):\*\* Nas chamadas seguintes ao \`desenfileirar()\`, enquanto a \`pilha\_saida\` mantiver elementos, não há transferência. O elemento da frente é removido diretamente com um único \`pop()\` da \`pilha\_saida\`, executado em tempo constante $O(1)$.

