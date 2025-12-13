from debugManager import debugManager, displayResults
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

    firstTime, firstMem = debug.measureWithTimeit(
        lambda: findValueBFSList(nodes, valueToSearch, valueOfNodes, startNode),
        runs=1000
    )
    debug.addFirstFunction(firstTime, firstMem)

    secondTime, secondMem = debug.measureWithTimeit(
        lambda: findValueBFS(nodes, valueToSearch, valueOfNodes, startNode),
        runs=1000
    )
    debug.addSecondFunction(secondTime, secondMem)

    resultFirst = findValueDFS(nodes, valueToSearch, valueOfNodes, startNode)
    resultSecond = findValueDFSList(nodes, valueToSearch, valueOfNodes, startNode)

    displayResults(debug, resultFirst, resultSecond, valueToSearch)
