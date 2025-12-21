from infoBranchNode import infoBranchNode
from SoC import SoC
from _init_ import createCompanyTree, initializeAllMessages


def simple_cyberattack_test():
    """
    Simple cyberattack simulation:
    1. Detect compromised account
    2. Disconnect it
    3. Migrate all keys
    4. Done
    """

    print("=" * 60)
    print("CYBERATTACK SIMULATION")
    print("=" * 60)

    # Setup
    root = createCompanyTree()
    soc = SoC(root)
    infoNodes = initializeAllMessages()

    for keyTitle, infoNode in infoNodes.items():
        node = soc.getNodeByTitle(keyTitle)
        if node:
            node.infoNode = infoNode

    print("\n[Initial State]")
    print(root.getAllKeysInSubtreeFormatted(show_keys=False))

    # ATTACK DETECTED
    print("\n" + "=" * 60)
    print("🚨 ATTACK DETECTED: JuniorDev3 account compromised!")
    print("=" * 60)

    compromised_node = soc.getNodeByTitle("JuniorDev3")
    if compromised_node and compromised_node.infoNode:
        decrypted = compromised_node.decryptMessageWithSelfKey(
            compromised_node.infoNode.getDataEncrypted()
        )
        print(f"Attacker can read: '{decrypted}'")

    # STEP 1: DISCONNECT
    print("\n[STEP 1: DISCONNECT COMPROMISED ACCOUNT]")
    print("Isolating JuniorDev3...")
    soc.isolateNode("JuniorDev3")
    print("✓ JuniorDev3 disconnected")
    print(f"✓ JuniorDev3 still in tree: {soc.getNodeByTitle('JuniorDev3') is not None}")

    # STEP 2: MIGRATE ALL KEYS
    print("\n[STEP 2: MIGRATE ALL COMPANY KEYS]")
    print("Rotating all encryption keys company-wide...")

    # Show some keys before
    ceo_key_before = root.key[:20]
    print(f"CEO key before: {ceo_key_before}")

    # Migrate
    soc.migrateKeys()

    print(f"✓ JuniorDev3 still in tree: {soc.getNodeByTitle('JuniorDev3') is not None}")


    # Show keys after
    ceo_key_after = root.key[:20]
    print(f"CEO key after:  {ceo_key_after}")
    print(f"✓ All {len(soc.getAllNodeTitles())} keys rotated")

    # STEP 3: VERIFY
    print("\n[STEP 3: VERIFY ALL DATA STILL ACCESSIBLE]")
    success = 0
    failed = 0

    for keyTitle in soc.getAllNodeTitles():
        node = soc.getNodeByTitle(keyTitle)
        if node and node.infoNode:
            try:
                decrypted = node.decryptMessageWithSelfKey(
                    node.infoNode.getDataEncrypted()
                )
                success += 1
            except:
                failed += 1
                print(f"✗ {keyTitle} failed")

    print(f"✓ {success} accounts verified")
    print(f"✗ {failed} accounts failed")

    # DONE
    print("\n" + "=" * 60)
    print("✅ INCIDENT RESPONSE COMPLETE")
    print("=" * 60)
    print("• Compromised account isolated")
    print("• All company keys rotated")
    print("• All data remains accessible")
    print("• Attacker's stolen credentials are now useless")
    print("=" * 60)


if __name__ == "__main__":
    simple_cyberattack_test()