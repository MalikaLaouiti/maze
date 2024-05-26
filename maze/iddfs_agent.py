from graphe import graphe
from pyamaze import maze, agent, COLOR

# Initialize the graph with a 10x10 maze
g = graphe(20, 20)

# Create the maze
g.m.CreateMaze()

# Convert the maze to a graph dictionary
graph_dict = g.maze_to_graph()



# Perform LDFS to find the path from start to end
found_iidfs, path_iidfs = g.iddfs((0, 0), (19, 19))  # Use (9, 9) for zero-based indexing

# Print if the path was found
print("LDFS Found:", found_iidfs)
print("Path LDFS:", path_iidfs)



path_4_based = [(i + 1, j + 1) for (i, j) in path_iidfs]
g.m.path=path_4_based
# Add the agent to the maze
a = agent(g.m, footprints=True, filled=True, color=COLOR.yellow)
# Trace the path on the maze
g.m.tracePath({a: g.m.path}, delay=300)

# Run the maze
g.m.run()
