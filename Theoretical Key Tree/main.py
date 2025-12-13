from cryptography.fernet import Fernet

from _init_ import initializeAllMessages, createCompanyTree
from classes import infoBranchNode, keyBranchNode, debugManager

# ---------------- Main ----------------

if __name__ == "__main__":
    # Get the tree with keys
    root = createCompanyTree()

    # Get just the messages
    messagesData = initializeAllMessages()

    # Now use root for tree operations
    print(root.getAllKeysInSubtreeFormatted(0))

    rootMessages = messagesData["Ceo"]

    print(rootMessages.getDataEncrypted())
    print(root.decryptMessageWithSelfKey(rootMessages.getDataEncrypted()))