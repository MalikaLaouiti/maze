from graphe import graphe
from pyamaze import maze, agent, COLOR

# Initialize the graph with a 10x10 maze
g = graphe(10, 10)

# Create the maze
g.m.CreateMaze()

# Convert the maze to a graph dictionary
graph_dict = g.maze_to_graph()
print(graph_dict)

# Perform DFS to find the path from start to end
found, path = g.dfs((0, 0), (9, 9))  # Use (9, 9) for zero-based indexing

# Print if the path was found
print("DFS Found:", found)
print("Path:", path)


if found:
    path_1_based = [(i + 1, j + 1) for (i, j) in path]
    g.m.path=path_1_based
    # Add the agent to the maze
    a = agent(g.m, footprints=True, filled=True, color=COLOR.blue)
    # Trace the path on the maze
    g.m.tracePath({a: g.m.path}, delay=300)

# Run the maze
g.m.run()
