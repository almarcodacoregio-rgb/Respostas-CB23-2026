import random
def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.
    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.
    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """

    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def dfs(x, y):
        maze[2*x+1][2*y+1] = room
        pilha = [(x, y)]

        while pilha:
            random.shuffle(directions)
            x, y = pilha[-1]

            for i in range(4):

                dx, dy = directions[i]
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and maze[2*nx+1][2*ny+1] == wall:
                    maze[2*x+1+dx][2*y+1+dy] = room
                    maze[2*nx+1][2*ny+1] = room
                    pilha.append((nx, ny))
                    break

                if i == 3: pilha.pop()


    #dfs(random.randint(1, m-1), random.randint(1, n-1))
    dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break


    def bfs_finder(_x, _y, target):
        fila = [(_x, _y, 0, 0)]
        path_history = {}

        cheese_arrow = None
        while cheese_arrow is None:

            x, y, edx, edy = fila.pop(0)
            path_history[(x, y)] = (edx, edy)
            random.shuffle(directions)

            for i in range(4):

                dx, dy = directions[i]
                nx, ny = x + dx, y + dy

                if 0 <= nx < 2*m+1 and 0 <= ny < 2*n+1 and maze[nx][ny] != wall and (dx, dy) != (-edx, -edy):
                    if maze[nx][ny] == target:
                        path_history[(nx, ny)] = (dx, dy)
                        cheese_arrow = (nx-dx, ny-dy)
                        break

                    if maze[nx][ny] == room:
                        fila.append((nx, ny, dx, dy))

        x, y = cheese_arrow

        maze[_x][_y] = "🐭"
        while (x, y) != (_x, _y):
            dx, dy = path_history[(x, y)]
            if (dx, dy) == (1, 0): maze[x][y] = "⬇️ "
            if (dx, dy) == (0, 1): maze[x][y] = "➡️ "
            if (dx, dy) == (-1, 0): maze[x][y] = "⬆️ "
            if (dx, dy) == (0, -1): maze[x][y] = "⬅️ "
            x -= dx; y -= dy


    bfs_finder(1, 1, cheese)


    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.
    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))


# Example usage:
if __name__ == '__main__':
    m, n = 20, 20  # Grid size
    #random.seed(1001100110010100)
    room   = '  '
    wall   = '🧱'
    cheese = '🧀'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)