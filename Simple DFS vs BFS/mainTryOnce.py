from degugManager import debugManager, displayResults
from searchAlgos import findValueDFS, findValueDFSList, findValueBFS, findValueBFSList

if __name__ == '__main__':

    nodes = []

    amountOfNodes = int(input("Enter amount of nodes: "))
    amountOfConnections = int(input("Enter amount of connections: "))

    for i in range(amountOfNodes):
        nodes.append([])

    connectionsInput = input("Enter all connections: ").split()

    for i in range(0, amountOfConnections * 2, 2):
        nodeToAddTo = int(connectionsInput[i])
        nodeToAdd = int(connectionsInput[i + 1])
        nodes[nodeToAddTo - 1].append(nodeToAdd - 1)

    print("Nodes Added")

    valueOfNodes = list(range(1, amountOfNodes + 1))

    print("\n--- Search Test ---")
    valueToSearch = int(input("Enter value to search for: "))
    startNode = 0

    debug = debugManager()

    debug.start("FirstFunction")
    resultFirst = findValueDFS(nodes, valueToSearch, valueOfNodes, startNode)
    debug.stop()

    debug.start("SecondFunction")
    resultSecond = findValueBFSList(nodes, valueToSearch, valueOfNodes, startNode)
    debug.stop()

    displayResults(debug, resultFirst, resultSecond, valueToSearch)