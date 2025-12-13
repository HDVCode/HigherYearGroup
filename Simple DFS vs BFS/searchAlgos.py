from collections import deque

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
