# Blockchain class  
class Blockchain (object):
    #constructor BlockChain : creates an initial empty list (to store blockchain) and other to store  transactions
    def __init__(self):
        self.chain=[]
        self.current_transaction=[]
    
    def new_block(self):
        #Method to create a new block and adds it to the chain (our blockchain)
        pass

    def new_transaction(self):
        #Method to add a new transaction to the list of transactions
        passed
    
    @staticmethod
    def hash(block):
        #hashes a Block
        pass

    #property 
    def last_block(self):
        #Return the last Block in the chain