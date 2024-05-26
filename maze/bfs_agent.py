from graphe import graphe
from pyamaze import maze, agent, COLOR

# Initialize the graph with a 10x10 maze
g = graphe(10, 10)

# Create the maze
g.m.CreateMaze()

# Convert the maze to a graph dictionary
graph_dict = g.maze_to_graph()



# Perform BFS to find the path from start to end
found_bfs, path_bfs = g.bfs((0, 0), (9, 9))  # Use (9, 9) for zero-based indexing

# Print if the path was found
print("BFS Found:", found_bfs)
print("Path BFS:", path_bfs)


if found_bfs:
    path_2_based = [(i + 1, j + 1) for (i, j) in path_bfs]
    g.m.path=path_2_based
    # Add the agent to the maze
    a = agent(g.m, footprints=True, filled=True, color=COLOR.red)
    # Trace the path on the maze
    g.m.tracePath({a: g.m.path}, delay=300)

# Run the maze
g.m.run()
