import os

import requests

API_URL = 'https://blockscout.com/etc/mainnet/graphiql'
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

# Specify the addresses and the current amount of transactions
CONTRACTS = {
    '0xc0971FF9b93e4AbCE2013E7B051f9c64a90D5DBA': 3,
    '0x1beef7795f9239De769c2e6dC0CFB432BAB86b87': 2,
    '0xA7d78E5108df90EAcD38Ad2a06A22c78dc8c1c46': 3,
    '0xfB9685B9daD350cD71fe203C13C4A3c8cc0f9BFE': 1,

}


def run_query(query):
    request = requests.post(API_URL, json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


for address, transactions in CONTRACTS.items():
    query = '''
    {{address(hash: "{address}") {{ fetchedCoinBalance, transactions(first: {transactions}) {{
      edges {{
        node {{
          id
        }}
      }}
    }} }} }}
    '''.format(address=address, transactions=transactions+1)

    result = run_query(query)
    no_of_transactions = len(result['data']['address']['transactions']['edges'])

    if no_of_transactions != transactions:
        print(f"Found change for address {address}")
        requests.post(WEBHOOK_URL, json={'value1': address, 'value2': no_of_transactions})