from collections import deque

# ------- Search Algos -------

def findValueDFSList(nodes, valueToFind, valueOfNodes, startNode):
    stack = [startNode]
    visited = set()

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if valueOfNodes[current] == valueToFind:
            return current

        for child in nodes[current]:
            stack.append(child)

    return -1


def findValueDFS(nodes, valueToFind, valueOfNodes, startNode):
    stack = deque([startNode])
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if valueOfNodes[current] == valueToFind:
            return current

        for child in nodes[current]:
            stack.append(child)

    return -1


def findValueDFSRecursive(nodes, valueToFind, valueOfNodes, currentNode, visited=None):
    if visited is None:
        visited = set()

    if currentNode in visited:
        return -1

    visited.add(currentNode)

    if valueOfNodes[currentNode] == valueToFind:
        return currentNode

    for child in nodes[currentNode]:
        result = findValueDFSRecursive(nodes, valueToFind, valueOfNodes, child, visited)

        if result != -1:
            return result

    return -1


def findValueBFSList(nodes, valueToFind, valueOfNodes, startNode):
    queue = [startNode]
    visited = set()

    while queue:
        current = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)

        if valueOfNodes[current] == valueToFind:
            return current

        for child in nodes[current]:
            queue.append(child)

    return -1


def findValueBFS(nodes, valueToFind, valueOfNodes, startNode):
    queue = deque([startNode])
    visited = set()

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if valueOfNodes[current] == valueToFind:
            return current

        for child in nodes[current]:
            queue.append(child)

    return -1
