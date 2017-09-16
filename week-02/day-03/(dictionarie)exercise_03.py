
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

accountCibBank = [
	{ 'client_name': 'Sanyi', 'account_number': 1123475543, 'balance': 203004099.2 },
	{ 'client_name': 'Jozsi', 'account_number': 6856787878, 'balance': 5204100071.23 },
	{ 'client_name': 'Bela', 'account_number': 8767868687, 'balance': 1353600.0 }
]

def printAccounts(randomverpistike):
    for accountDict in randomverpistike:
        print(accountDict)

def getAccount(accountsLocal, accountNumberToQuery):
    for accountDict in accountsLocal:
        if accountDict["account_number"] == accountNumberToQuery:
            return accountDict

    print("404 - account not found")

def transfer(accoutnsLocal, fromAccountNumber, toAccountNumber, amount):
    accFrom = getAccount(accoutnsLocal, fromAccountNumber)
    accTo   = getAccount(accoutnsLocal, toAccountNumber)

    if accFrom != None and accFrom != None and accFrom != accTo:
        if accFrom['balance'] >= amount:
            accFrom['balance'] -= amount
            accTo['balance']   += amount


# accountNumberFrom = int(input('Enter account number from: '))
# print(type(accountNumberFrom))
# accountNumberTo = int(input('Enter account number to: '))

# printAccounts(accountCibBank)
# transfer(accountCibBank, accountNumberFrom, accountNumberTo, 2313)
# printAccounts(accountCibBank)

class BankAccount:
    accountName = ''
    accountNumber =0
    balance=0

    def __init__(self, name, number, balance):
        self.accountName = name
        self.accountNumber = number
        self.balance = balance

    def transfer(self, amount):
        self.balance += amount

    def printMe(self):
        print(self.accountName)
        print(self.balance)

sanyi = BankAccount("Sanyi", 213123, 21)
print (sanyi)
print(type(sanyi))
sanyi.transfer(10)
sanyi.printMe()

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist


# def all_info(name):
#     client = input('Please enter your name: ')
#     for i in name:
#         if i['client_name'] == client:
#             return i
#         # elif ['client_name'] != client:
#         #     print('Wrong name')

# def client_balance(balance):
#     client = all_info(accounts)
#     print(client['balance'])
#     trasfer_to = input('Please enter who do you want to trasfer: ')
#     if client['client_name'] == transfer_to['client_name']:
#         trasfer_from['client_name'] += transfer_to['client_name']
#         transfer_to['client_name'] -= trasfer_from['client_name']
        
#     return client

# def transfer(amout):
#     for i in client_balance(accounts):

#     
# def name_of_client():
#     for 


# print("Given account number is: ", accountNumber)
# print(queryNameAndBalance(accounts, accountNumber))

#print(client_balance(accounts))
