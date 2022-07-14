
    #methods
        # see all of our members 
        # highest account holder 
        
# Account
    # name 
    # balance
    
class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
    def addAccount(self):
        newName = input("what is the account holder's name? >>")
        newBalance = float(input("how much money do you have(for real)? >>"))
        accountObj = Account(newName, newBalance)
        self.accounts.append(accountObj)
    def search(self):
        query = input("who's account would you like to access? >>")
        for account in self.accounts:
            if query == account.name:
                print(account.name, account.balance)
    def totalBankBalance(self):
        sum = 0
        for account in self.accounts:
            sum += account.balance
        print(f'the total balance of the bank is {sum}')
    def allMembers(self):
        for account in self.accounts:
            print(account.name, account.balance)
    def highestAccount(self):
        highestAmount = self.accounts[0].balance
        for account in self.accounts:
            if account.balance > highestAmount:
                highestAmount = account.balance
        print(highestAmount)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

chase=Bank("Chase", "123 Chase St.")
chase.addAccount()
chase.addAccount()
chase.addAccount()
chase.allMembers()