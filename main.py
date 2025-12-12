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


# ---------------- debugManager class ----------------

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


    def getAllKeysInSubtreeFormatted(self, level=0):

        indent = "    " * level
        result = f"{indent}{self.keyTitle}: {self.key}\n"

        for child in self.children:

            result += child.getAllKeysInSubtreeFormatted(level + 1)

        return result


    def decryptMessageWithSelfKey(self, message):

        return decrypt(self.key, message)


    def decryptMessageWithSubNodesKeyDFS(self, message, keyUsed, debug=None, top=True):

        if top and debug:

            debug.start("DFS")

        if self.keyTitle == keyUsed:

            result = decrypt(self.key, message)

        else:

            result = -1

            for child in self.children:

                res = child.decryptMessageWithSubNodesKeyDFS(message, keyUsed, debug=debug, top=False)

                if res != -1:

                    result = res
                    break

        if top and debug:

            debug.stop()

        return result


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


# ---------------- Main ----------------

def main():

    key = b"QLxJ3wK9Uizg_3NpNO0nfBaUMoPxQX5hcck-RTSF2v4="
    root = keyBranchNode("Root", key)

    encrypted_message = "gAAAAABpOyADJxM5cGbIlaorCMMlD98JFYci7BLY1EyYk-sfrJ6yOvwtSaHSil0yvh-RF_FNQOsvyQTqKSXsDjtbo11gM0ogdKVK0c48eH7c87eRiYGJh9R7RqUI5-WZBNk-qx9P1YbGBfIa_qbULIhIKiE_KB1E1A=="
    rootMessage = infoBranchNode(encrypted_message, root.getKeyTitle())

    key = b"ouJxMsNqe5a3bSWqY1Wilo2BGPq5kR5HevYJmEXRJ4U="
    HrOfHrOfHr = keyBranchNode("HrOfHrOfHr", key)

    encrypted_message = "gAAAAABpOyNhHY7MrmLp_85a6cc_s2tKgiH4bTnB8gCZrozcga9axUXKgoOGN-MAZ6wMhpCh-VMvWOVhQyyr_gJ6h4q021noomjyNhZt03x2KuXi2P8uXUA="
    HrOfHrOfHrMessage = infoBranchNode(encrypted_message, HrOfHrOfHr.getKeyTitle())

    key = b"r-KUinF8v2hIJy192vtouz_zdNjubV8XHi2tdaldVts="
    HrOfHr = keyBranchNode("Root", key)

    encrypted_message = "gAAAAABpOyQYhiZK5FsnsHmWEsbcHuQ0nadM1ThWY1ZQtS8RcwQGtw-kE5RH1_EdeQV2PCn3igm7ttjCATKJbbX3lYgW3H3DCb_Av8YrnA0IDT5UtVPaRSI="
    HrOfHrMessage = infoBranchNode(encrypted_message, root.getKey())

    print(root.decryptMessageWithSelfKey(rootMessage.getDataEncrypted()))
    print(HrOfHrOfHr.decryptMessageWithSelfKey(HrOfHrOfHrMessage.getDataEncrypted()))
    print(HrOfHr.decryptMessageWithSelfKey(HrOfHrMessage.getDataEncrypted()))


if __name__ == "__main__":
    main()
