from collections import deque
from encryption import decrypt


# ---------------- keyBranchNode ----------------

class keyBranchNode:

    def __init__(self, keyTitle, key):

        self.keyTitle = keyTitle
        self.key = key
        self.children = []
        self.infoNode = None


    def changeName(self, newName):
        self.keyTitle = newName

    def addChild(self, newBranchNode):
        self.children.append(newBranchNode)

    def removeChild(self, newBranchNode):
        self.children.remove(newBranchNode)

    def getKey(self):
        return self.key

    def getKeyTitle(self):
        return self.keyTitle

    def getChildren(self):
        return self.children


    def getAllKeysInSubtreeFormatted(self, show_keys=False, prefix=""):
        result = prefix + self.keyTitle

        if show_keys:
            result += f": {self.key}"

        result += "\n"

        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                new_prefix = prefix + "    └── "
            else:
                new_prefix = prefix + "    ├── "
            # Recursive call for child
            result += child.getAllKeysInSubtreeFormatted(show_keys, new_prefix)

        return result


    def decryptMessageWithSelfKey(self, message):

        return decrypt(self.key, message)


    def decryptMessageWithSubNodesKeyDFSRecursive(self, message, keyUsed):

        if self.keyTitle == keyUsed:

            result = decrypt(self.key, message)

        else:

            result = -1

            for child in self.children:

                res = child.decryptMessageWithSubNodesKeyDFSRecursive(message, keyUsed)

                if res != -1:

                    result = res
                    break

        return result


    def decryptMessageWithSubNodesKeyDFS(self, message, keyUsed):

        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == keyUsed:

                return decrypt(node.key, message)

            stack.extend(reversed(node.children))

        return -1


    def decryptMessageWithSubNodesKeyBFS(self, message, keyUsed):

        if self.keyTitle == keyUsed:

            result = decrypt(self.key, message)

        else:

            queueOfSubNodesLeft = deque(self.children)
            result = -1

            while queueOfSubNodesLeft:

                node = queueOfSubNodesLeft.popleft()

                if node.keyTitle == keyUsed:

                    result = decrypt(node.key, message)
                    break

                for child in node.children:

                    queueOfSubNodesLeft.append(child)

        return result


    def getChildReferenceDFS(self, title):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == title:
                return node

            stack.extend(reversed(node.children))

        return None
