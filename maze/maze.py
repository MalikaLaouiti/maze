from graphe import graphe
from pyamaze import maze, agent, COLOR
class graphe:
    def __init__(self, rows, cols):
        self.m = maze(rows, cols)
        self.g = {}

    def maze_to_graph(self):
        for i in range(self.m.rows):
            for j in range(self.m.cols):
                self.g[(i, j)] = []
                if j + 1 < self.m.cols and not self.m.maze_map[(i + 1, j + 1)]['E']:  # Check East
                    self.g[(i, j)].append((i, j + 1))
                if j - 1 >= 0 and not self.m.maze_map[(i + 1, j + 1)]['W']:  # Check West
                    self.g[(i, j)].append((i, j - 1))
                if i - 1 >= 0 and not self.m.maze_map[(i + 1, j + 1)]['N']:  # Check North
                    self.g[(i, j)].append((i - 1, j))
                if i + 1 < self.m.rows and not self.m.maze_map[(i + 1, j + 1)]['S']:  # Check South
                    self.g[(i, j)].append((i + 1, j))
        return self.g

    def succ(self, node):
        return self.g[node]

    def dfs(self, x, y):
        p = []
        self.A = []
        self.E = []
        self.E.append(x)
        B = []
        p.append(x)
        while len(p) > 0:
            curr = p.pop()
            B.append(curr)
            if curr == y:
                return True, B
            else:
                for i in self.succ(curr):
                    if i not in self.E:
                        p.append(i)
                        self.E.append(i)
        return False, B


# Initialize the graph with a 10x10 maze
g = graphe(10, 10)

# Create the maze
g.m.CreateMaze()

# Convert the maze to a graph dictionary
graph_dict = g.maze_to_graph()
print("Graph Dictionary:", graph_dict)

# Perform DFS to find the path from start to end
found, path = g.dfs((0, 0), (9, 9))  # Use (9, 9) for zero-based indexing

# Print if the path was found
print("DFS Found:", found)
print("Path:", path)

if found:
    path_1_based = [(i + 1, j + 1) for (i, j) in path]
    print("Path (1-based):", path_1_based)
    
    # Add the agent to the maze
    a = agent(g.m, footprints=True, filled=True, color=COLOR.blue)
    
    # Trace the path on the maze
    g.m.tracePath({a: path_1_based}, delay=300)
else:
    print("No path found")

# Run the maze
g.m.run()
