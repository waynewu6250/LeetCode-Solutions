a = ['###...##..',
     '....#....#',
     '#..###.#.#',
     'S#.#.#.#..',
     '...#...E#.']

matrix = []
for i, line in enumerate(a):
    for j, num in enumerate(line):
        if num == 'S':
            start = (i,j)
    matrix.append([s for s in line.strip('\n')])

queue = [start]
visited = set([start])
father = [[0]*len(matrix[0]) for _ in range(len(matrix))]

while queue:
    
    x, y = queue.pop(0)
    
    flag = 0
    for (x_inc, y_inc) in [(0,1), (0,-1), (1,0), (-1,0)]:
        x_new = x + x_inc
        y_new = y + y_inc
        if 0 <= x_new < len(matrix) and 0 <= y_new < len(matrix[0]) and matrix[x_new][y_new] == 'E':
            # backtrack
            x_old, y_old = x, y
            while matrix[x_old][y_old] != 'S':
                matrix[x_old][y_old] = '*'
                x_old, y_old = father[x_old][y_old]
            for line in matrix:
                print(line)
            queue = []
            
        if 0 <= x_new < len(matrix) and \
           0 <= y_new < len(matrix[0]) and \
           matrix[x_new][y_new] == '.' and \
           (x_new, y_new) not in visited:
            queue.append((x_new, y_new))
            visited.add((x_new, y_new))
            father[x_new][y_new] = (x, y)

print('Trapped')