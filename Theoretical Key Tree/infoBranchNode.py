from cryptography.fernet import Fernet


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

    def transferKeyRaw(self, oldKeyBytes, newKeyBytes):
        try:
            decrypted = Fernet(oldKeyBytes).decrypt(self.data)
            self.data = Fernet(newKeyBytes).encrypt(decrypted)

        except Exception:
            pass
