import random
N = random.randint(4, 7)
grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
while True:
    src = (random.randint(0, N-1), random.randint(0, N-1))
    goal = (random.randint(0, N-1), random.randint(0, N-1))
    if src != goal and grid[src[0]][src[1]] == 0 and grid[goal[0]][goal[1]] == 0:
        break

for i in range(N):
    row = []
    for j in range(N):
        if (i, j) == src:
            row.append("S")
        elif (i, j) == goal:
            row.append("G")
        else:
            row.append(str(grid[i][j]))
    print(" ".join(row))

stack = [src]
visited = set()
parent = {src: None}
order = []

while stack:
    node = stack.pop()
    if node in visited:
        continue
    visited.add(node)
    order.append(node)
    if node == goal:
        break
    x, y = node
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    random.shuffle(neighbors)
    for nx, ny in neighbors:
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0 and (nx, ny) not in visited and (nx, ny) not in parent:
            stack.append((nx, ny))
            parent[(nx, ny)] = node

path = []
node = goal
while node is not None:
    path.append(node)
    node = parent.get(node)
path.reverse()

print("\nDFS Path:", path if path and path[0] == src else "No path found")
print("Topological Order of Node Traversal:", order)
