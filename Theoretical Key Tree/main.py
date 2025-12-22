from _init_ import createCompanyTree, initializeAllMessages
from SoC import SoC
from keyBranchNode import keyBranchNode
from encryption import encrypt, decrypt
from cryptography.fernet import Fernet


# ---------------- Colors ----------------

def printRed(text):
    print(f"\033[91m{text}\033[0m")

def printGreen(text):
    print(f"\033[92m{text}\033[0m")

def printBlue(text):
    print(f"\033[94m{text}\033[0m")

def printYellow(text):
    print(f"\033[93m{text}\033[0m")


# ---------------- Setup ----------------

def attachInfoNodes(root, infoNodes):
    stack = [root]
    while stack:
        node = stack.pop()
        if node.keyTitle in infoNodes:
            node.infoNode = infoNodes[node.keyTitle]
        stack.extend(node.children)


# ---------------- Global Session State ----------------

hacker_current_node = None
worker_current_node = None
root = None
backup = None


# ---------------- Shared User Session ----------------

def user_session(soc, label, initial_node=None):
    current = initial_node

    if current is None:
        print(f"\n{label} INITIAL ACCESS\n")

        print(soc.getAllKeysInSubtreeFormatted())

        start = input("\nNode identity: ")
        current = soc.getNodeByTitle(start)

        if not current:
            printRed("Invalid identity")
            return None
    else:
        print(f"\n{label} SESSION RESUMED")

    while True:

        if label == "WORKER":
            printYellow(f"\n{label} CURRENT NODE: {current.keyTitle}")

            print("1. Show accessible subtree")
            print("2. See message")
            print("3. See sub-message")
            print("4. Traverse")
            print("5. Edit data")
            print("0. Exit session")

            choice = input("> ")

            if choice == "1":
                print(current.getAllKeysInSubtreeFormatted(show_keys=False))

            elif choice == "2":
                if current.infoNode:
                    try:
                        message = current.decryptMessageWithSelfKey(current.infoNode.getDataEncrypted())
                        printGreen(message)
                    except Exception:
                        printRed("Decryption failed")
                else:
                    printYellow("No data attached")

            elif choice == "3":
                target = input("Target message owner: ")
                result = current.decryptMessageWithSubNodesKey(target)

                if result != -1:
                    printGreen(result)
                else:
                    printRed("Key not accessible")

            elif choice == "4":
                print("\nReachable nodes:")
                print(current.getAllKeysInSubtreeFormatted(show_keys=False))

                destination = input("Move to:\n> ")
                newNode = current.getChildReference(destination)

                if newNode:
                    current = newNode
                    printGreen("Moved within subtree")
                else:
                    printRed("Node not reachable")

            elif choice == "5":
                if not current.infoNode or not current.key:
                    printYellow("No editable message")
                    continue

                new_text = input("\nEnter new content:\n> ")
                current.infoNode.data = encrypt(current.key, new_text)
                printGreen("Message updated")

            elif choice == "0":
                return current

        else:
            printRed(f"\n{label} CURRENT NODE: {current.keyTitle}")

            print("1. Show accessible subtree")
            print("2. Decrypt self message")
            print("3. Decrypt message using subnode key")
            print("4. Traverse")
            print("5. Edit data")
            print("0. Exit session")

            choice = input("> ")

            if choice == "1":
                print(current.getAllKeysInSubtreeFormatted(show_keys=False))

            elif choice == "2":
                if current.infoNode:
                    try:
                        message = current.decryptMessageWithSelfKey(current.infoNode.getDataEncrypted())
                        printGreen("Decrypted: " + message)
                    except Exception:
                        printRed("Decryption failed")
                else:
                    printYellow("No data attached")

            elif choice == "3":
                target = input("Target message owner: ")
                result = current.decryptMessageWithSubNodesKey(target)

                if result != -1:
                    printGreen("Decrypted: " + result)
                else:
                    printRed("Key not accessible")

            elif choice == "4":
                print("\nReachable nodes (subtree only):")
                print(current.getAllKeysInSubtreeFormatted(show_keys=False))

                destination = input("Move to:\n> ")
                newNode = current.getChildReference(destination)

                if newNode:
                    current = newNode
                    printGreen("Moved within subtree")
                else:
                    printRed("Node not reachable")

            elif choice == "5":
                if not current.infoNode or not current.key:
                    printYellow("No editable message")
                    continue

                new_text = input("\nEnter new content (encrypted on write):\n> ")
                current.infoNode.data = encrypt(current.key, new_text)
                printGreen("Message updated (still encrypted)")

            elif choice == "0":
                return current


# ---------------- Hacker Perspective ----------------

def hacker_session(soc):
    global hacker_current_node
    hacker_current_node = user_session(soc, label="HACKER", initial_node=hacker_current_node)


# ---------------- Worker Perspective ----------------

def worker_session(soc):
    global worker_current_node
    worker_current_node = user_session(soc, label="WORKER", initial_node=worker_current_node)


# ---------------- SOC Perspective ----------------

def soc_session(soc):

    global backup

    while True:
        printBlue("\nSOC MODE")
        print("1. Show subtree")
        print("2. Quarantine node")
        print("3. Quarantine subtree")
        print("4. Rekey entire tree")
        print("5. Backup tree")
        print("6. Redirect traffic")
        print("7. Create honeypot")
        print("8. Honeypot spam")
        print("9. Purge honeypots")
        print("0. Exit SOC mode")

        choice = input("> ")

        if choice == "1":
            print(soc.getAllKeysInSubtreeFormatted())

        elif choice == "2":
            target = input("Node to quarantine: ")
            if soc.isolateNode(target):
                printGreen("Done")
            else:
                printRed("Failed")

        elif choice == "3":
            target = input("Subtree root: ")
            if soc.quarantineSubtree(target):
                printGreen("Done")
            else:
                printRed("Failed")

        elif choice == "4":
            soc.migrateKeys()
            printGreen("Entire tree rekeyed")

        elif choice == "5":
            backup = soc.backupTree()
            printYellow("Backup stored")

        elif choice == "6":
            from_node = input("From node: ")
            to_node = input("To node: ")
            if soc.redirectTraffic(from_node, to_node):
                printGreen("Traffic redirected")
            else:
                printRed("Failed")

        elif choice == "7":
            target = input("Target node: ")
            honeypot = soc.createHoneypot(target)
            if honeypot:
                printYellow("Honeypot deployed: " + honeypot.keyTitle)
            else:
                printRed("Invalid target")

        elif choice == "8":
            target = input("Target node: ")
            for i in range(1000):
                honeypot = soc.createHoneypot(target, 5)
                if honeypot:
                    printYellow("Honeypot deployed: " + honeypot.keyTitle)
                else:
                    printRed("Invalid target")

        elif choice == "9":
            count = soc.purgeHoneypots()
            printGreen(f"Purged {count} honeypot nodes")

        elif choice == "0":
            break


# ---------------- System / Admin Perspective ----------------

def system_session(soc):

    global root

    while True:
        printGreen("\nSYSTEM / ADMIN MODE")
        print("1. Create node")
        print("2. Remove node")
        print("3. Add child node")
        print("4. Remove child node")
        print("5. Show subtree")
        print("0. Exit system mode")

        choice = input("> ")

        if choice == "1":
            name = input("New node name: ")
            parent_name = input("Parent node: ")

            parent = soc.getNodeByTitle(parent_name)

            if parent:
                new_node = keyBranchNode(name, Fernet.generate_key())
                parent.addChild(new_node)

                soc.nodeMap[name] = new_node
                soc.parentMap[new_node] = parent

                printGreen("Node created")
            else:
                printRed("Parent not found")

        elif choice == "2":
            name = input("Node to remove: ")

            node = soc.getNodeByTitle(name)

            parent = soc.parentMap[node]
            parent.removeChild(node)

            soc.parentMap.pop(name, None)
            soc.nodeMap.pop(name, None)

        elif choice == "3":
            parent = input("Parent: ")
            child = input("Child: ")
            soc.nodeMap[parent].addChild(soc.nodeMap[child])

        elif choice == "4":
            parent = input("Parent: ")
            child = input("Child: ")

            soc.nodeMap[parent].removeChild(soc.nodeMap[child])

        elif choice == "5":
            print(soc.getAllKeysInSubtreeFormatted())

        elif choice == "0":
            break


# ---------------- Main ----------------

def main():

    global root

    root = createCompanyTree()
    infoNodes = initializeAllMessages()
    attachInfoNodes(root, infoNodes)

    soc = SoC(root)
    root = soc.root

    while True:
        print("\n==== SYSTEM ====")
        printRed("1. Hacker perspective")
        printBlue("2. SOC perspective")
        printYellow("3. Worker perspective")
        printGreen("4. System / Admin perspective")
        print("0. Exit")

        choice = input("> ")

        if choice == "1":
            hacker_session(soc)
        elif choice == "2":
            soc_session(soc)
        elif choice == "3":
            worker_session(soc)
        elif choice == "4":
            system_session(soc)
        elif choice == "0":
            break


if __name__ == "__main__":
    main()