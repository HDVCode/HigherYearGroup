from keyBranchNode import keyBranchNode
from cryptography.fernet import Fernet


# ---------------- Encryption / Decryption ----------------

# Encrypts a message with a key and outputs the result
def encrypt(key, message):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypts a message with a key and outputs the result
def decrypt(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()



# ----------------  SoC ----------------

class SoC:

    def __init__(self, root):
        """
        Initialize SoC with a keyBranchNode tree root
        """
        self.root = root
        self.nextHandle = 0
        self.nodeMap = {}  # Maps keyTitle to node reference
        self.parentMap = {}  # Maps node → parent
        self.backupRoot = None  # Backup tree

        self._buildNodeMap(root, None)

    def copySubtree(self, node):
        newNode = keyBranchNode(node.keyTitle, node.key)

        # Copy the info node reference too!
        newNode.infoNode = node.infoNode

        for child in node.children:
            newChild = self.copySubtree(child)
            newNode.children.append(newChild)

        return newNode


    def backupTree(self):

        return self.copySubtree(self.root)

    def restoreTree(self, backupRoot):

        self.root = backupRoot
        self.nodeMap = {}
        self.parentMap = {}
        self._buildNodeMap(self.root, None)


    def _buildNodeMap(self, node, parent):
        self.nodeMap[node.keyTitle] = node
        self.parentMap[node] = parent
        for child in node.children:
            self._buildNodeMap(child, node)


    def addNodeReference(self, parentNode, childNode):

        if childNode not in parentNode.children:
            parentNode.children.append(childNode)
            self.parentMap[childNode] = parentNode
            return True

        return False


    def removeNodeReference(self, parentNode, childNode):

        if childNode in parentNode.children:
            parentNode.children.remove(childNode)
            self.parentMap[childNode] = None
            return True

        return False


    def isolateNode(self, keyTitle):

        if keyTitle not in self.nodeMap:
            return False

        targetNode = self.nodeMap[keyTitle]

        parent = self.parentMap.get(targetNode)

        if parent:

            for child in targetNode.children:
                self.addNodeReference(parent, child)

            self.removeNodeReference(parent, targetNode)

        return True

    def detachSubtree(self, targetNode):

        for child in targetNode.children:
            self.parentMap[child] = None
            self.detachSubtree(child)

        self.parentMap[targetNode] = None


    def redirectTraffic(self, fromKeyTitle, toKeyTitle):

        if fromKeyTitle not in self.nodeMap or toKeyTitle not in self.nodeMap:
            return False

        fromNode = self.nodeMap[fromKeyTitle]
        toNode = self.nodeMap[toKeyTitle]

        parent = self.parentMap.get(fromNode)

        if not parent:
            return False

        for i, child in enumerate(parent.children):
            if child == fromNode:
                parent.children[i] = toNode
                self.parentMap[toNode] = parent
                break

        return True


    def quarantineSubtree(self, keyTitle):

        if keyTitle not in self.nodeMap:
            return []

        targetNode = self.nodeMap[keyTitle]
        quarantined = []

        def collectSubtree(node):
            quarantined.append(node.keyTitle)
            for child in node.children:
                collectSubtree(child)

        collectSubtree(targetNode)
        self.isolateNode(keyTitle)

        return quarantined


    def createHoneypot(self, keyTitle):
        if keyTitle not in self.nodeMap:
            return False

        honeypotKey = Fernet.generate_key()
        honeypotNode = keyBranchNode(f"Honeypot_{keyTitle}", honeypotKey)

        return honeypotNode


    def getNodeByTitle(self, keyTitle):
        return self.nodeMap.get(keyTitle, None)


    def getAllNodeTitles(self):
        return list(self.nodeMap.keys())

    def changeKeyTitle(self, nodeTitle, newKeyTitle):
        if nodeTitle not in self.nodeMap:
            return False

        if newKeyTitle in self.nodeMap:
            return False

        node = self.nodeMap[nodeTitle]

        # Changed: infoNode is now singular, not a list
        if node.infoNode:
            node.infoNode.editKeyUsed(newKeyTitle)

        del self.nodeMap[nodeTitle]
        node.changeName(newKeyTitle)
        self.nodeMap[newKeyTitle] = node

        return True


    def rekeyNodeWithInfo(self, keyTitle):
        if keyTitle not in self.nodeMap:
            return False

        keyNode = self.nodeMap[keyTitle]

        oldKeyBytes = keyNode.key
        newKeyBytes = Fernet.generate_key()
        keyNode.key = newKeyBytes

        # Changed: infoNode is now singular, not a list
        if keyNode.infoNode:
            keyNode.infoNode.transferKeyRaw(oldKeyBytes, newKeyBytes)
            keyNode.infoNode.keyUsed = keyTitle

        return True

    def migrateKeys(self):

        backupRoot = self.backupTree()

        # Save all info nodes before restoring
        saved_info_nodes = {}
        for keyTitle, node in self.nodeMap.items():
            if node.infoNode:
                saved_info_nodes[keyTitle] = node.infoNode

        # Restore tree structure
        self.restoreTree(backupRoot)

        # Reattach info nodes
        for keyTitle, infoNode in saved_info_nodes.items():
            node = self.getNodeByTitle(keyTitle)
            if node:
                node.infoNode = infoNode

        # Now rekey everything
        def recurse(node):
            self.rekeyNodeWithInfo(node.keyTitle)
            for child in node.children:
                recurse(child)

        recurse(self.root)