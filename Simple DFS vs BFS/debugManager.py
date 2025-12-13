import matplotlib.pyplot as plt
import numpy as np
import timeit
import tracemalloc


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