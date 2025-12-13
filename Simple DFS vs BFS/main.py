from degugManager import debugManager, displayResults
from searchAlgos import findValueDFS, findValueBFS

# ------ Main ------

if __name__ == '__main__':

    # Build graph structure
    nodes = []

    amountOfNodes = int(input("Enter amount of nodes: "))
    amountOfConnections = int(input("Enter amount of connections: "))

    for i in range(amountOfNodes):
        nodes.append([])

    connections_input = input("Enter all connections: ").split()

    for i in range(0, amountOfConnections * 2, 2):
        nodeToAddTo = int(connections_input[i])
        nodeToAdd = int(connections_input[i + 1])
        nodes[nodeToAddTo - 1].append(nodeToAdd - 1)

    print("Nodes Added")

    valueOfNodes = list(range(1, amountOfNodes + 1))

    # Search setup
    print("\n--- Search Test ---")
    valueToSearch = int(input("Enter value to search for: "))
    startNode = 0

    debug = debugManager()

    # Run DFS
    debug.start("DFS")
    resultDFS = findValueDFS(nodes, valueToSearch, valueOfNodes, startNode)
    debug.stop()

    # Run BFS
    debug.start("BFS")
    resultBFS = findValueBFS(nodes, valueToSearch, valueOfNodes, startNode)
    debug.stop()

    # ------- Dont look at this lol -------

    displayResults(debug, resultDFS, resultBFS, valueToSearch)

