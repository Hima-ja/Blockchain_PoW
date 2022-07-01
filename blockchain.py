import hashlib
import json
import datetime
from uuid import uuid4
from flask import Flask
class Dexter_Blockchain(object):
    def __init__(self):
        #Initially the chain is empty
        self.chain = []
        #Stores the current transactions go into this list
        self.current_transactions = []
        #Stores the amount each participant has in the blockchain
        self.balance = []
        #All the validated transactions go into this list
        self.validated_transactions = []
        self.flag = 0
    def new_block(self,proof=100,previous_hash=None):
        if(len(self.chain)==0):
            #Creates the genesis block
                block = {
                'index':len(self.chain) + 1,
                'timestamp':datetime.datetime.now(),
                'transactions':self.validated_transactions[:3],
                'proof':100,
                'previous_hash':0
            }
                self.chain.append(block)
                del self.validated_transactions [:3]
                #Reset the list of transactions 
                self.current_transactions = []
                return block

        else:
        #Creates a new block and adds it to the chain.
             block = {
                'index':len(self.chain) + 1,
                'timestamp':datetime.datetime.now(),
                'transactions':self.validated_transactions[:3],
                'proof':proof,
                'previous_hash':self.hash(self.chain[-1])
            }
             self.chain.append(block)
             del self.validated_transactions [:3]
            #Reset the list of transactions 
             self.current_transactions = []
             return block
    def proof_of_work(self, previous_proof):
        proof = 1
        valid_proof = False
         
        while proof is False:
            hash_operation = hashlib.sha256(
                str(proof - previous_proof).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                valid_proof = True
            else:
                proof += 1
                 
        return proof
    def Customers_Data(self):
        #We store the data of who owns how much in the list
        try:
            Participant = str(input("Enter the name of the participant: "))
            fund = float(input("Enter the value of currency you own: "))
            self.balance.append({
                            'Participant':Participant,
                            'Balance': fund,
                            }
                        )
        except:
            print("The format of data you entered is not valid!")
    def Print_Customers_data(self):
        #Prints the data of the currency each participant has
        for index in range(len(self.balance)):
                for key in self.balance[index]:
                    print(self.balance[index][key])


    def create_transaction(self):
        #Taking the inputs of the transaction data
        try:
            sender = str(input("Enter the name of the sender: "))
            recepient = str(input("Enter the name of the receiver: "))
            amount = float(input("Enter the amount to be transferred: "))
            self.current_transactions.append({
                        #Transaction ID is a random number generated for the unique identification of the transaction
                        'Transaction_ID':str(uuid4()).replace('-', ''),
                        'Timestamp':datetime.datetime.now(),
                        'Sender':sender,
                        'Recipient':recepient,
                        'Amount': amount,
                    })
            print("The transaction is added to the current pool of transactions")
            print("........validating the following transaction")
        except:
            print("The format you gave as input is invalid")
    def validate_transaction(self):
        #We search for the sender in the customer's list and compare the currency he owns with the amount he want to send to the recipient
        for high in range(len(self.balance)):
                #If the amount to be transferred is less than the sender's balance, the transaction is invalidated
                    if(self.current_transactions[-1]["Sender"]==self.balance[high]["Participant"]):
                            if(self.current_transactions[-1]["Amount"]>self.balance[high]["Balance"]):
                                print("The transaction with the transaction ID " + self.current_transactions[-1]["Transaction_ID"] + " is invalid")
                                break
                #If the amount to be transferred is more than the sender's balance,the transaction is validated and the required operations take place
                            else:
                                self.balance[high]["Balance"]-=self.current_transactions[-1]["Amount"]
                                self.flag  = 1
                                for res in range(len(self.balance)):
                                    if(self.current_transactions[-1]["Recipient"]==self.balance[res]["Participant"]):
                                        self.balance[res]["Balance"]+=self.current_transactions[-1]["Amount"]
                                self.validated_transactions.append(self.current_transactions[-1])
                                print("The transaction with the transaction ID " + self.current_transactions[-1]["Transaction_ID"] + " is validated")
                                break

               

#Used to validate the blockchain
    def chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            #Compare the hash of the previous block and the attribute of the previous hash in the present block 
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(previous_proof*proof).encode()).hexdigest()
            #If the hash operation doesn't give the required output
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index+=1
        return True

    @staticmethod
    def hash(block):
        #Creating a SHA-256 hash of a block
        #We must make sure that the dictionary is ordered,or we will have inconsistent hashes
        block_string = json.dumps(block,sort_keys = True,default=str).encode()
        return hashlib.sha256(block_string).hexdigest()
    @property
    def last_block(self):
        #Returns the last block in the chain
        return self.chain[-1]

blockchain = Dexter_Blockchain()
menu = {}
menu['1']="Add a new customer(node) to the database(blockchain network): " 
menu['2']="Create a new transaction: "
menu['3']="Print the data of who owns how much"
menu['4']= "Create a new block"
menu['5']= "Print the existing blocks"
menu['6'] = "Exit the program"
while True: 
  options=menu.keys()
  print("Hello Dexter!!!!!!!")
  for choice in options: 
      print (choice,menu[choice])
  selection = input("Select the required operation:")
  if selection == '1':
      blockchain.Customers_Data()
      print("The following person was successfully added to the network")
  elif selection == '2':
      blockchain.create_transaction()
      blockchain.validate_transaction()
      if(blockchain.flag==1):
            wish = input("Do you want the receipt of this transaction:  Yes/No  ")
            if(wish=="Yes"):
                  print(blockchain.validated_transactions[-1])
            else:
                print("Thank you and visit again!")

  elif selection=='3':
      blockchain.Print_Customers_data()
  elif selection=='4':
      if(len(blockchain.validated_transactions)<3):
                #Since we took that the maximum transactions a block can hold is 3
                print("Do more transactions in order to create a block")
      else:
          if(len(blockchain.chain)>1):
            blockchain.proof_of_work(blockchain.chain[-1]["proof"])
            blockchain.new_block()
            print(blockchain.chain[-1])
          else:
            #Creating a Genesis Block
            blockchain.new_block()
            print(blockchain.chain[-1])

      
    
  elif selection=='5':
     print(blockchain.chain)
  elif selection=='6':
      break
  else:
      print("Invalid option selected!")

  
