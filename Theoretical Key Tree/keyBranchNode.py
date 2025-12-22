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


    def decryptMessageWithSubNodesKey(self, keyUsed):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == keyUsed and node.infoNode:
                return decrypt(
                    node.key,
                    node.infoNode.getDataEncrypted()
                )

            stack.extend(reversed(node.children))

        return -1

    def getChildReference(self, title):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == title:
                return node

            stack.extend(reversed(node.children))

        return None

