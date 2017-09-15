
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist


def all_info(name):
    client = input('Please enter your name: ')
    for i in name:
        if i['client_name'] == client:
            return i
        # elif ['client_name'] != client:
        #     print('Wrong name')

def client_balance(balance):
    client = all_info(accounts)
    print(client['balance'])
    trasfer_to = input('Please enter who do you want to trasfer: ')
    if client['client_name'] == transfer_to['client_name']:
        trasfer_from['client_name'] += transfer_to['client_name']
        transfer_to['client_name'] -= trasfer_from['client_name']
        
    return client

def transfer(amout):
    for i in client_balance(accounts):

#     
# def name_of_client():
#     for 
print(client_balance(accounts))