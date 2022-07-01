Blockchain_PoW
# Project Scenario(Description):
Dexter owns a coffee shop. As his coffee shop is very famous, the logbooks are prone to change. He needs his transactions to be immutable and safe. Hence, he uses a block chain to keep a track of his transactions and the history of the transactions to be safe. The purpose of this project is to help Dexter implement the block chain in order for the transaction history to be immutable and many more.Security is also one of the most essential feature to be implemented correctly. For this very reason, we need to implement a consensus algorithm in the blockchain. More about it in the later part.
# A glance on the emerging technology of Blockchain:
The block chain is basically a distributed database. It’s distributed. It’s open source, so anyone can change the underlying code, and they can see what’s going on. It’s truly peer to peer.It uses state-of-the-art cryptography, so if we have a global, distributed database that can record the fact that we’ve done this transaction and also it could record any structured information, not just who paid whom but also who married whom or who owns what land, etc. In the case of the Internet of Things, we’re going to need a block chain-settlement system underneath. Banks won’t be able to settle trillions of real-time transactions between things. So, this is an extraordinary thing. An immutable, unhackable distributed database of digital assets. This is a platform for truth and it’s a platform for trust.
# A glance on the concept of consensus algorithms:
We all know that block chain is a peer-to-peer network. It is essential for the network to reach for an agreement in the crucial aspects of the block chain. In order to do that, we have consensus algorithms which is an agreement between all the nodes in the network to agree upon the true state of the block chain.
It is also the main reason why block chains are so secure even in the absence of a central authority. These algorithms achieve reliability in the block chain network and establish trust between unknown peers in the distributed computing environment of block chain. It makes sure that every new block that is added to the block chain is the one and only true version of truth that is agreed upon by all the nodes in the block chain.

In this project,we use the well-known consensus algorithm Proof of Work(PoW).
# Execution
Step-1: Run the file blockchain.py
 
Step-2: Select the required option according to the function you require
For example, if we press 1, we are asked to enter the name of the participant and the account balance. In this way, we can store the participants and the currency they possess.
Ex:
![image](https://user-images.githubusercontent.com/86017986/176829938-82c443f4-d98b-43ae-bf83-c06be6df1c84.png)


We press 2 when we want to create a transaction and validate it. We can also print the receipt as per their interest
Ex:
![image](https://user-images.githubusercontent.com/86017986/176829961-9df0634f-d158-428a-9efb-91d14899e41c.png)

We press 3 when we want to know the currency that each person in the network has.
Ex:
 
![image](https://user-images.githubusercontent.com/86017986/176829983-a4d204de-e502-4f29-8491-22cda16195e1.png)
 

We press 4 when we want to create a new block. Ex:

![image](https://user-images.githubusercontent.com/86017986/176830009-5a20fc65-de2b-487b-abcc-b8152a7df0ef.png)

We press 5 when we want to print the block chain. Ex:

![image](https://user-images.githubusercontent.com/86017986/176830031-d431d7a3-c216-4c15-93bb-67d8c8dd2ed9.png)

 
We press 6 to exit the program.
# Functionalities
1.Dexter has information regarding all the available blocks.
Each block has a hash, hash of the previous block, timestamp of the block, a unique id of the block (nonce).All of them are accessible to Dexter.
 
Example:
 ![image](https://user-images.githubusercontent.com/86017986/176830056-1e403d3d-9541-442a-8fb7-8045acde8f3b.png)


2.None	of	Dexter's	friends	should	be	able	to	edit	the	added transactions.
Each block has a hash and the hash of the previous hash. If any of them try to edit the transactions, the hash of the block and as well as the previous blocks also gets changed. It’s very difficult to calculate all the hashes. Hence, it’s almost impossible to edit the added transactions.
In the below screenshot, we can see the previous_hash of the block
![image](https://user-images.githubusercontent.com/86017986/176830123-a4213890-b0e2-4b75-b167-aa190387efa0.png)


3.Timestamp of each transaction is readily available.
When we print the transaction data, we can know the exact date and time at which the transaction took place. In the below screenshot we can also see the timestamp of the transactions.

4.Dexter should have all the information regarding the completed transactions.
Each transaction has a sender, recipient, amount, timestamp and the transaction Id. We can get an instant receipt of the transaction.
Ex:
![image](https://user-images.githubusercontent.com/86017986/176830171-08d000e8-b8a2-4d09-ba9e-6fe764954618.png)

This is the menu which we use to perform various operations.
 
 ![image](https://user-images.githubusercontent.com/86017986/176830199-b7f35745-a6dd-4b5d-9b28-489dc22d6f0a.png)




# Contributors
Himaja Sai Dama (2019A3PS0464H) Chaitanya Yadav (2019AAPS0296H) Bhavitha Lakkireddy (2019AAPS0222H)

