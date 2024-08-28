import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # create the genesis block
        self.new_block(previous_hash = 1, proof = 100)

    def new_block(self, proof, previous_hash=None):
        # creates a new block and adds it to the chain
        """
        create a new block in the block chain
        :param proof: <int> the proof given by the proof of work algorithm
        :param previous_hash: (optional) <str> hash of the previous block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):
        # adds a new transaction to the list of transactions
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> address of the sender
        :param recipient: <str> address of the recipient
        :param amount: <int> amount
        :return: <int> the index of the block that will hold this transaction
        """
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a block
        """
        Create a SHA-256 hash of a block
        :param block: <dict> Block
        :return: <str>
        """
        # convert the block which is a dict into a JSON formatted string
        json_block = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(json_block).hexdigest()

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm:
        - find a number q' such that hash(qq') contains leading 4 zeros, where q is the previous q'
        - q is the previous proof, and q' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

            return proof
        
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess[:4] == "0000"


