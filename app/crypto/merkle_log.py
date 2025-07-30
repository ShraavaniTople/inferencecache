from pymerkle import MerkleTree, InmemoryTreeStorage

# Use in-memory storage for now
storage = InmemoryTreeStorage()
tree = MerkleTree(hash_type="sha256", storage=storage)

def add_to_merkle(data: str):
    """
    Add a new AI output to the Merkle Tree.
    Returns the current root and a proof of inclusion.
    """
    leaf = data.encode()
    proof = tree.append_entry(leaf)
    return {
        "root": tree.root_hash,
        "proof": proof.hexproof,
        "index": proof.leaf_index
    }

def get_merkle_root():
    return tree.root_hash
