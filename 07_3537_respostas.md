\*\*Matrícula:\*\* 3537  

\#\#\# Justificativa Teórica (Questão 2\)

Como o labirinto gerado é \*\*perfeito\*\* (estrutura de árvore sem ciclos e com caminho único entre quaisquer duas células), tanto a Busca em Largura (BFS) quanto a Busca em Profundidade (DFS) encontrariam a solução. O caminho final percorrido até o queijo é idêntico em ambas as abordagens.

A escolha pelo \*\*BFS\*\* para a etapa de solução justifica-se por dois fatores principais:

1\. \*\*Comportamento e Eficiência de Busca:\*\* Enquanto o DFS se aprofunda em um único caminho — correndo o risco de percorrer becos sem saída extensos caso a escolha inicial de direção seja desfavorável —, o BFS expande em ondas de distância a partir da origem. Isso garante que o número de células exploradas dependa diretamente da distância entre o ponto inicial \`(1, 1)\` e o queijo, tornando a busca mais previsível e eficiente quando o objetivo está próximo.

2\. \*\*Complementaridade Algorítmica:\*\* Como a geração do labirinto (Questão 1\) utilizou o DFS iterativo com suporte de uma \*\*Pilha (LIFO)\*\*, a adoção do BFS para o pathfinding permitiu explorar a aplicação prática de uma \*\*Fila (FIFO)\*\*, demonstrando o contraste entre o aprofundamento com backtracking e a expansão por camadas.  
