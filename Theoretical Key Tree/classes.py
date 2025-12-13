from cryptography.fernet import Fernet
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import timeit
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
        self.firstFunctionTimeLog = []
        self.firstFunctionSpaceLog = []
        self.secondFunctionTimeLog = []
        self.secondFunctionSpaceLog = []

    def measureWithTimeit(self, func, runs=1000):
        avgTime = timeit.timeit(func, number=runs) / runs

        tracemalloc.start()
        func()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return avgTime, peak / 1024

    def addFirstFunction(self, timeVal, memVal):
        self.firstFunctionTimeLog.append(timeVal)
        self.firstFunctionSpaceLog.append(memVal)

    def addSecondFunction(self, timeVal, memVal):
        self.secondFunctionTimeLog.append(timeVal)
        self.secondFunctionSpaceLog.append(memVal)

    def getLastFirstFunction(self):
        if self.firstFunctionTimeLog:
            return self.firstFunctionTimeLog[-1], self.firstFunctionSpaceLog[-1]
        return None, None

    def getLastSecondFunction(self):
        if self.secondFunctionTimeLog:
            return self.secondFunctionTimeLog[-1], self.secondFunctionSpaceLog[-1]
        return None, None

    def plotComparison(self, label):
        x = np.arange(1)
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.firstFunctionTimeLog, width, label='First Function Time')
        ax.bar(x + width / 2, self.secondFunctionTimeLog, width, label='Second Function Time')
        ax.set_ylabel('Time (seconds)')
        ax.set_title('First Function vs Second Function Search Time')
        ax.set_xticks(x)
        ax.set_xticklabels([label])
        ax.legend()
        plt.show()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(x - width / 2, self.firstFunctionSpaceLog, width, label='First Function Space')
        ax.bar(x + width / 2, self.secondFunctionSpaceLog, width, label='Second Function Space')
        ax.set_ylabel('Memory (KB)')
        ax.set_title('First Function vs Second Function Peak Memory')
        ax.set_xticks(x)
        ax.set_xticklabels([label])
        ax.legend()
        plt.show()


def displayResults(debug, resultFirstFunc, resultSecondFunc, valueToSearch):

    firstTime, firstMemory = debug.getLastFirstFunction()
    secondTime, secondMemory = debug.getLastSecondFunction()

    print(f"\nFirst Function: {'Found at node ' + str(resultFirstFunc + 1) if resultFirstFunc != -1 else 'Not found'}")
    print(f"     Time: {firstTime:.9f}s | Memory: {firstMemory:.2f} KB")

    print(f"\nSecond Function: {'Found at node ' + str(resultSecondFunc + 1) if resultSecondFunc != -1 else 'Not found'}")
    print(f"     Time: {secondTime:.9f}s | Memory: {secondMemory:.2f} KB")

    if firstTime and secondTime:
        speedup = firstTime / secondTime
        print(f"\nSpeedup: {speedup:.2f}x {'(Second faster)' if speedup > 1 else '(First faster)'}")

    debug.plotComparison(f"Search for value {valueToSearch}")

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
