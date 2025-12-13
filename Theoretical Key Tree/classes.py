from cryptography.fernet import Fernet
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import time
import tracemalloc


# ---------------- Encryption / Decryption ----------------

# Encrypts a message with a key and outputs the result
def encrypt(key, message):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypts a message with a key and outputs the result
def decrypt(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()


# Class in charge of managing the debug
class debugManager:

    def __init__(self):

        self.method = None
        self.startTime = None
        self.dfsTimeLog = []
        self.dfsSpaceLog = []

        self.bfsTimeLog = []
        self.bfsSpaceLog = []


    # Start measuring the debug stuff
    def start(self, method):

        self.startTime = time.perf_counter()
        tracemalloc.start()

        self.method = method


    # Stop measuring the debug stuff
    def stop(self):

        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if self.method == "DFS":

            self.dfsTimeLog.append(end - self.startTime)
            self.dfsSpaceLog.append(peak / 1024)  # KB

        elif self.method == "BFS":

            self.bfsTimeLog.append(end - self.startTime)
            self.bfsSpaceLog.append(peak / 1024)


    # Get last measurement of DFS debug
    def get_last_dfs(self):
        if self.dfsTimeLog:
            return self.dfsTimeLog[-1], self.dfsSpaceLog[-1]
        return None, None

    # Get last measurement of BFS debug
    def get_last_bfs(self):
        if self.bfsTimeLog:
            return self.bfsTimeLog[-1], self.bfsSpaceLog[-1]
        return None, None


    # Clear all past debug info
    def clear(self):

        self.dfsTimeLog.clear()
        self.dfsSpaceLog.clear()
        self.bfsTimeLog.clear()
        self.bfsSpaceLog.clear()

    # Plot comparing the current BFS vs DFS info gathered
    def plotComparison(self, keys):
        x = np.arange(len(keys))
        width = 0.35

        # --- Time plot ---
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.dfsTimeLog, width, label='DFS Time')  # fixed variable name
        ax.bar(x + width / 2, self.bfsTimeLog, width, label='BFS Time')  # fixed variable name
        ax.set_ylabel('Time (seconds)')
        ax.set_title('DFS vs BFS Decryption Time per Key')
        ax.set_xticks(x)
        ax.set_xticklabels(keys)
        ax.legend()
        plt.show()

        # --- Space plot ---
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.dfsSpaceLog, width, label='DFS Space')  # fixed variable name
        ax.bar(x + width / 2, self.bfsSpaceLog, width, label='BFS Space')  # fixed variable name
        ax.set_ylabel('Memory (KB)')
        ax.set_title('DFS vs BFS Peak Memory per Key')
        ax.set_xticks(x)
        ax.set_xticklabels(keys)
        ax.legend()
        plt.show()


# ---------------- infoBranchNode ----------------

# The class holding all the info (encrypted)
class infoBranchNode:

    def __init__(self, data, keyUsed):
        self.data = data
        self.keyUsed = keyUsed


    def getDataEncrypted(self):
        return self.data


    def editData(self, data):
        self.data = data


    def getKeyUsed(self):
        return self.keyUsed


    def editKeyUsed(self, keyUsed):
        self.keyUsed = keyUsed


# ---------------- keyBranchNode ----------------

class keyBranchNode:

    def __init__(self, keyTitle, key):

        self.keyTitle = keyTitle
        self.key = key
        self.children = []

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


    def decryptMessageWithSubNodesKeyDFSRecursive(self, message, keyUsed, debug=None, top=True):

        if top and debug:

            debug.start("DFS")

        if self.keyTitle == keyUsed:

            result = decrypt(self.key, message)

        else:

            result = -1

            for child in self.children:

                res = child.decryptMessageWithSubNodesKeyDFSRecursive(message, keyUsed, debug=debug, top=False)

                if res != -1:

                    result = res
                    break

        if top and debug:

            debug.stop()

        return result


    def decryptMessageWithSubNodesKeyDFS(self, message, keyUsed, debug=None):

        if debug:
            debug.start("DFS")

        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == keyUsed:

                if debug:
                    debug.stop()

                return decrypt(node.key, message)

            stack.extend(reversed(node.children))

        if debug:
            debug.stop()

        return -1


    def decryptMessageWithSubNodesKeyBFS(self, message, keyUsed, debug=None):

        if debug:

            debug.start("BFS")

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

        if debug:

            debug.stop()

        return result


    def getChildReferenceDFS(self, title):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.keyTitle == title:
                return node

            stack.extend(reversed(node.children))

        return None
