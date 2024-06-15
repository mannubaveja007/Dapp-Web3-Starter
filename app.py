from flask import Flask, render_template
from web3 import Web3

app = Flask(__name__)

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/c1f1949736784147be468d66f3550727'))
assert w3.provider.is_connected()

# Your smart contract's address and ABI
contract_address = '0x1ccb1BdDC8C876cA3e1C5Fd8c0045D9fE57CcDFE'
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "getMessage",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "message",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Create a contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect_wallet')
def connect_wallet():
    # Logic to connect to the user's wallet
    #...
    return render_template('wallet.html')

@app.route('/count')
def count():
    # message = contract.functions.getMessage().call()
    str=input("[+] Enter String to print : ")
    return render_template('count.html', message=str)

if __name__ == '__main__':
    app.run(debug=True)