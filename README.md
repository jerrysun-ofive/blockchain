### Basic Blockchain Implementation In Python

# 🕹️ Introduction

This repository contains a simple implementation of blockchain using Python. The aim of the project was to help me understand the core concepts of blockchain, including blocks, transactions, proof of work, hashing, aswell as the immutability and sequential nature of blockchains.

# 🛠️ Features
- Blockchain Structure: A basic blockchain that stores a sequence of blocks, containing a list of transactions.
- Genesis Block: Automatically creates the first block in the blockchain with predefined proof and previous hash.
- New Transaction: Allows adding new transactions to be included in the next mined (or generated) block
- Proof of Work: Implements a simple proof of work algorithm requiring a hash with leading 4 zeros. The difficulty of the PoW can be increased by increaseing the needed leading zeros needed, .e.g to 8 leading zeros.
- Block Hashing: Using SHA-256 to hash blocks, ensuring integrity.

---

# 🪄 Installation
To run this project, you'll  need to have Python installed on your system
1. Clone this repository:
`git clone https://github.com/yourusername/blockchain.git`
2. Navigate to the project directory:
`cd blockchain`
3. Run the code using Python:
`python3 blockchain.py`
