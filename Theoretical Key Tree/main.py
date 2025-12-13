from _init_ import initializeAllMessages, createCompanyTree

# ---------------- Main ----------------

def main():
    # Get the tree with keys
    root = createCompanyTree()

    # Get just the messages
    messagesData = initializeAllMessages()

    # Now use root for tree operations
    print(root.getAllKeysInSubtreeFormatted(0))

    rootMessages = messagesData["HrHead"]

    print(rootMessages.getDataEncrypted())
    print(root.decryptMessageWithSubNodesKeyDFS(rootMessages.getDataEncrypted(), rootMessages.getKeyUsed()))

if __name__ == "__main__":
    main()