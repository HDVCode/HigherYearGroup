from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import time
import tracemalloc


# ----- Debug Manager -----

class debugManager:

    def __init__(self):
        self.method = None
        self.startTime = None
        self.dfsTimeLog = []
        self.dfsSpaceLog = []
        self.bfsTimeLog = []
        self.bfsSpaceLog = []

    def start(self, method):
        self.startTime = time.perf_counter()
        tracemalloc.start()
        self.method = method

    def stop(self):
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if self.method == "DFS":
            self.dfsTimeLog.append(end - self.startTime)
            self.dfsSpaceLog.append(peak / 1024)
        elif self.method == "BFS":
            self.bfsTimeLog.append(end - self.startTime)
            self.bfsSpaceLog.append(peak / 1024)

    def get_last_dfs(self):
        if self.dfsTimeLog:
            return self.dfsTimeLog[-1], self.dfsSpaceLog[-1]
        return None, None

    def get_last_bfs(self):
        if self.bfsTimeLog:
            return self.bfsTimeLog[-1], self.bfsSpaceLog[-1]
        return None, None

    def plotComparison(self, label):
        x = np.arange(1)
        width = 0.35

        # Time plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.dfsTimeLog, width, label='DFS Time')
        ax.bar(x + width / 2, self.bfsTimeLog, width, label='BFS Time')
        ax.set_ylabel('Time (seconds)')
        ax.set_title('DFS vs BFS Search Time')
        ax.set_xticks(x)
        ax.set_xticklabels([label])
        ax.legend()
        plt.show()

        # Space plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.dfsSpaceLog, width, label='DFS Space')
        ax.bar(x + width / 2, self.bfsSpaceLog, width, label='BFS Space')
        ax.set_ylabel('Memory (KB)')
        ax.set_title('DFS vs BFS Peak Memory')
        ax.set_xticks(x)
        ax.set_xticklabels([label])
        ax.legend()
        plt.show()


# ------- Search Algos -------

def findValueDFS(nodes, valueToFind, valueOfNodes, startNode):
    stack = [startNode]
    visited = set()

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if valueOfNodes[current] == valueToFind:
            return current

        for child in reversed(nodes[current]):
            stack.append(child)

    return -1


def findValueBFS(nodes, valueToFind, valueOfNodes, startNode):

    queue = deque([startNode])
    visited = {startNode}

    while queue:
        currentNode = queue.popleft()

        if valueOfNodes[currentNode] == valueToFind:
            return currentNode

        for childNode in nodes[currentNode]:
            if childNode not in visited:
                visited.add(childNode)
                queue.append(childNode)

    return -1


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

    # Display results
    dfsTime, dfsMemory = debug.get_last_dfs()
    bfsTime, bfsMemory = debug.get_last_bfs()

    print(f"\nDFS: {'Found at node ' + str(resultDFS + 1) if resultDFS != -1 else 'Not found'}")
    print(f"     Time: {dfsTime:.6f}s | Memory: {dfsMemory:.2f} KB")

    print(f"\nBFS: {'Found at node ' + str(resultBFS + 1) if resultBFS != -1 else 'Not found'}")
    print(f"     Time: {bfsTime:.6f}s | Memory: {bfsMemory:.2f} KB")

    # Show comparison
    debug.plotComparison(f"Search for value {valueToSearch}")